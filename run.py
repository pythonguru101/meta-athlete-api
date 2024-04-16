from flask import Flask, request
from flask_restful import Api
from flask_jwt_extended import JWTManager
from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask_apispec.extension import FlaskApiSpec
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.dialects.mysql import FLOAT
from flask_cors import CORS
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
UPLOADS_FOLDER = os.path.join(APP_ROOT, 'app/static/uploads')
ATHLETE_IMAGE_UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/static/althleteimages')
ATHLETE_VIDEO_UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/static/althletevideos')
META_ATHLETE_IMAGE_UPLOAD_FOLDER = os.path.join(APP_ROOT, 'app/static/metaathletesimages')


app = Flask(__name__)
CORS(app, supports_credentials=True)
api = Api(app)
app.config.from_object('config.ProductionConfig')
app.config['UPLOADS_FOLDER'] = UPLOADS_FOLDER
app.config['ATHLETE_IMAGE_UPLOAD_FOLDER'] = ATHLETE_IMAGE_UPLOAD_FOLDER
app.config['ATHLETE_VIDEO_UPLOAD_FOLDER'] = ATHLETE_VIDEO_UPLOAD_FOLDER
app.config['META_ATHLETE_IMAGE_UPLOAD_FOLDER'] = META_ATHLETE_IMAGE_UPLOAD_FOLDER
PREFIX = "/api/v1"

app.config.update({
    'APISPEC_SPEC': APISpec(
        title='Health Service',
        version='v1',
        plugins=[MarshmallowPlugin()],
        openapi_version='2.0.0'
    ),
    'APISPEC_SWAGGER_URL': '/api/v1/doc/',  # URI to access API Doc JSON 
    'APISPEC_SWAGGER_UI_URL': '/api/v1/doc-ui/'  # URI to access UI of API Doc
})
docs = FlaskApiSpec(app)
jwt = JWTManager(app)

db = SQLAlchemy(app)

@app.before_first_request
def create_tables():
    db.create_all()

from app.controllers import (
    file, 
    # member,
    nft_athlete_card_marketplace,
    nft_athlete_card,
    nft_avaialable_athlete_card_tier,
    user,
)

def create_endpoints(api, docs, prefix):

    # File
    api.add_resource(file.UploadFile, prefix + '/uploadfile')
    docs.register(file.UploadFile)

    # # Member endpoints
    # api.add_resource(member.AlthleteAdd, prefix + '/members_add')
    # api.add_resource(member.AllAthlete, prefix + '/members')
    # api.add_resource(member.AthleteBase, prefix + '/members/<int:p_id>')
    # docs.register(member.AllAthlete)
    # docs.register(member.AlthleteAdd)
    # docs.register(member.AthleteBase)

    # NFT Card Tier
    api.add_resource(nft_avaialable_athlete_card_tier.AvailableCardsModelAdd, prefix + '/nftcardstier_add')
    api.add_resource(nft_avaialable_athlete_card_tier.AllAthleteCard, prefix + '/nftcardstier')
    api.add_resource(nft_avaialable_athlete_card_tier.AthleteCardBase, prefix + '/nftcardstier/<int:p_id>')
    docs.register(nft_avaialable_athlete_card_tier.AllAthleteCard)
    docs.register(nft_avaialable_athlete_card_tier.AvailableCardsModelAdd)
    docs.register(nft_avaialable_athlete_card_tier.AthleteCardBase)

    # NFT Athlete Card
    api.add_resource(nft_athlete_card.MetaAlthleteAdd, prefix + '/nftathletecard_add')
    api.add_resource(nft_athlete_card.AllMetaAthlete, prefix + '/nftathletecard')
    api.add_resource(nft_athlete_card.MetaAthleteBase, prefix + '/nftathletecard/<int:p_id>')
    docs.register(nft_athlete_card.AllMetaAthlete)
    docs.register(nft_athlete_card.MetaAlthleteAdd)
    docs.register(nft_athlete_card.MetaAthleteBase)

    # NFT Marketplace
    api.add_resource(nft_athlete_card_marketplace.NFTMarketplaceAdd, prefix + '/nftmarketplace_add')
    api.add_resource(nft_athlete_card_marketplace.AllNFTMarketplace, prefix + '/nftmarketplace')
    api.add_resource(nft_athlete_card_marketplace.NFTMarketplaceBase, prefix + '/nftmarketplace/<int:p_id>')
    docs.register(nft_athlete_card_marketplace.NFTMarketplaceAdd)
    docs.register(nft_athlete_card_marketplace.AllNFTMarketplace)
    docs.register(nft_athlete_card_marketplace.NFTMarketplaceBase)

    # User
    api.add_resource(user.UserAdd, prefix + '/users_add')
    api.add_resource(user.AllUser, prefix + '/users')
    api.add_resource(user.UserBase, prefix + '/users/<int:p_id>')
    docs.register(user.UserAdd)
    docs.register(user.AllUser)
    docs.register(user.UserBase)
    
create_endpoints(api, docs, PREFIX)
