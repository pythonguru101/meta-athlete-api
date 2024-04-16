from flask_restful import Resource, reqparse, inputs
from app.models.nft_athlete_card_marketplace import NFTMarketplaceModel
from app.models.nft_avaialable_athlete_card_tier import AvailableCardsModel
from app.models.nft_athlete_card import MetaAthleteNFT
from flask_jwt_extended import jwt_required
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from werkzeug.datastructures import FileStorage  
from werkzeug.utils import secure_filename
from marshmallow import Schema, fields
from run import app


parser = reqparse.RequestParser()
parser.add_argument('wallet_id', help='Wallet id foreign key field required', required=True)
parser.add_argument('tier', help='Tier field required', required=True)
parser.add_argument('price', help='Price field required', required=True)
parser.add_argument('athlete_card_id', help='Athlete card foreign key field required', required=True)


class NFTMarketplaceAdd(MethodResource, Resource):
    @doc(description='This resource for this endpoint /nftmarketplace_add for save data into database',
        version='1.0',
        tags=['Meta Athletes Card Primitive']
    )
    def post(self):
        try:
            data = parser.parse_args()
            
            # Validates if the athlete card added exists
            exists =  MetaAthleteNFT.find_by_id(data['athlete_card_id'])
            if not exists:
                return {'message': 'Athlete card does not exist'}, 400

            new_meta_card_athlete = NFTMarketplaceModel(
                wallet_id = data['wallet_id'],
                tier = data['tier'],
                price = data['price'],
                athlete_card_id = data['athlete_card_id']  
            )
            new_meta_card_athlete.save_to_db() 
            jsonify_data = NFTMarketplaceModel.to_json(new_meta_card_athlete)
            return jsonify_data
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500     
            
class AllNFTMarketplace(MethodResource, Resource):
    """this resource for /metaathlets_card endpoint by this url all data can view"""

    @doc(description=' This resource for /metaathletscard endpoint by this url all data can view ',
        version='1.0',
        tags=['Meta Athletes Card Primitive']
    )
    def get(self):
        try:
            return NFTMarketplaceModel.return_all()
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class NFTMarketplaceBase(MethodResource, Resource):
    """this resource for /metaathletscard/<int:p_id> endpoint by this url classes data can update, delete, single data view """

    @doc(
        description=' this resource for /metaathletscard/<int:p_id> endpoint by this url classes data can single data view ',
        version='1.0',
        tags=['Meta Athletes Card Primitive']
    )
    def get(self, p_id):
        try:
            get_data = NFTMarketplaceModel.find_by_id(p_id)
            if not get_data:
                return {'message': 'Meta Athlete Card not found'}, 400
            jsonify_data = NFTMarketplaceModel.to_json(get_data)
            jsonify_data["athlete"] = MetaAthleteNFT.to_json(get_data.athlete)
            return jsonify_data
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
