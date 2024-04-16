from flask_restful import Resource, reqparse
from flask_apispec import doc
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from app.models.user import UserModel
from run import app


parser = reqparse.RequestParser()
parser.add_argument('username', help='Username required', required=True)
parser.add_argument('password', help='Password required', required=True)
parser.add_argument('wallet_id', help='Wallet id required', required=True)
parser.add_argument('did', help='DID is optional', required=False)
parser.add_argument('vc', help='VC is optional', required=False)


class UserAdd(MethodResource, Resource):
    def post(self):
        try:
            data = parser.parse_args()

            new_user = UserModel(
                username = data["username"],
                password = data["password"],
                wallet_id = data["wallet_id"],
                did = data["did"],
                vc = data["vc"],
            )

            new_user.save_to_db() 
            jsonify_data = new_user.to_json(new_user)
            return jsonify_data
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class AllUser(MethodResource, Resource):
    @doc(description=' This resource for /users endpoint by this url all data can view ',
        version='1.0',
        tags=['Athlete']
    )
    def get(self):
        try:
            return UserModel.return_all()
        except Exception as e:
            return {'message': 'Something went wrong'}, 500


class UserBase(MethodResource, Resource):
    """this resource for /users/<int:p_id> endpoint by this url classes data can update, delete, single data view """
    
    @doc(
        description=' this resource for /users/<int:p_id> endpoint by this url classes data can single data view ',
        version='1.0',
        tags=['User'])
    def get(self, p_id):
        try:
            get_data = UserModel.find_by_id(p_id)
            if not get_data:
                return {'message': 'User not found'}, 400
            jsonify_data = get_data.to_json(get_data)
            return jsonify_data
        except Exception as e:
            return {'message': 'Something went wrong'}, 500

    @doc(description=' this resource for /althletes/<int:p_id> endpoint by this url classes data can delete ',
        version='1.0',
        tags=['Athlete']
    )
    def delete(self, p_id):
        try:
            get_data = UserModel.find_by_id(p_id)
            if get_data:
                get_data.db_to_delete()
                return {'message': ' Data deleted successfully'}, 200
            else:
                return {'message': 'Data not found'}, 400
        except Exception as e:
            return {'message': 'Something went wrong'}, 500

    @doc(description=' this resource for /althletes/<int:p_id> endpoint by this url classes data can update ',
        version='1.0',
        tags=['Athlete']
    )
    def put(self, p_id):
        try:
            get_data = UserModel.find_by_id(p_id)

            data = parser.parse_args()
                
            new_user = UserModel(
                user_type = data["name"],
                wallet_id = data["wallet_id"],
            )
            
            if get_data:
                get_data.update_data(get_data, new_user)

                get_data.db_to_commit()
                jsonify_data = get_data.to_json(get_data)
                return jsonify_data
            else:
                return {'message': 'User not found'}, 400
        except Exception as e:
            return {'message': 'Something went wrong'}, 500




