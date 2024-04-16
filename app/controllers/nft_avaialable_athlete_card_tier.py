from flask_restful import Resource, reqparse
from app.models.nft_avaialable_athlete_card_tier import AvailableCardsModel
# from app.models.member import Member
from app.models.nft_athlete_card import MetaAthleteNFT
from flask_jwt_extended import jwt_required
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from utils.enums import CardType
from run import app


parser = reqparse.RequestParser()
parser.add_argument('card_number', help='Card Number field required', required=True)
parser.add_argument('tier', help='Tier field required', required=True)
parser.add_argument('id_nft', help='Id NFT field required', required=True)


class AvailableCardsModelResponseSchema(Schema):
    card_number = fields.Int(default='None')
    tier = fields.Str(default='None')
    id_nft = fields.Int(default='None')


class AvailableCardsModelRequestSchema(Schema):
    card_number = fields.Int(required=True, description="Card Number field is required")
    tier = fields.Str(required=True, description="Tier field is required")
    id_nft = fields.Int(required=True, description="Id NFT field is required")


class AvailableCardsModelAdd(MethodResource, Resource):
    """ this resource for this endpoint /althletecards_add for save data into database"""

    @doc(description='This resource for this endpoint /althletecards_add for save data into database',
        version='1.0',
        tags=['Available Cards Model']
    )
    def post(self):
        try:
            data = parser.parse_args()
            tier = CardType.fetch_items(data['tier'])
            if not tier:
                return {'message': 'Invalid tier'}, 400
            
            # Verify if id_nft exists
            id_nft = MetaAthleteNFT.find_by_id(data['id_nft'])
            if not id_nft:
                return {'message': 'The specified Athlete does not exist'}, 400
            
            new_athlete_card = AvailableCardsModel(
                card_number = data['card_number'],
                tier = tier,
                id_nft = data['id_nft'],
            )

            new_athlete_card.save_to_db()
            jsonify_data = AvailableCardsModel.to_json(new_athlete_card)
            return {"data": jsonify_data}
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class AllAthleteCard(MethodResource, Resource):
    """this resource for /althletecards endpoint by this url all data can view"""

    @doc(description=' This resource for /althletecards endpoint by this url all data can view ',
        version='1.0',
        tags=['Available Cards Model']
    )
    def get(self):
        try:
            return AvailableCardsModel.return_all()
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class AthleteCardBase(MethodResource, Resource):
    """this resource for /althletecards/<int:p_id> endpoint by this url classes data can update, delete, single data view """

    @doc(
        description=' this resource for /althletecards/<int:p_id> endpoint by this url classes data can single data view ',
        version='1.0',
        tags=['Available Cards Model']
    )
    def get(self, p_id):
        try:
            get_data = AvailableCardsModel.find_by_id(p_id)
            if not get_data:
                return {'message': 'Data not found'}, 400
            jsonify_data = AvailableCardsModel.to_json(get_data)
            return jsonify_data
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    @doc(description=' this resource for /althletecards/<int:p_id> endpoint by this url data can delete ',
        version='1.0',
        tags=['Available Cards Model']
    )
    def delete(self, p_id):
        try:
            get_data = AvailableCardsModel.find_by_id(p_id)
            if get_data:
                get_data.db_to_delete()
                return {'message': ' Data deleted successfully'}, 200
            else:
                return {'message': 'Athlete card not found'}, 400
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500

    @doc(description=' this resource for /althletecards/<int:p_id> endpoint by this url data can update ',
        version='1.0',
        tags=['Athlete Card']
    )
    def put(self, p_id):
        try:
            data = parser.parse_args()
            get_data = AvailableCardsModel.find_by_id(p_id)
            if get_data:
                get_data.update_data(get_data, data)
                tier = CardType.fetch_items(data['tier'])
                if not tier:
                    return {'message': 'Invalid card type'}, 400
            else:
                return {'message': 'Athlete card not found'}, 400

            get_data.db_to_commit()
            jsonify_data = AvailableCardsModel.to_json(get_data)
            return jsonify_data
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
