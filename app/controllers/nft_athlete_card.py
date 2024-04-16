from flask_restful import Resource, reqparse, inputs
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from werkzeug.datastructures import FileStorage

from utils.enums import SportType, SchoolGrade, UserType
from utils.common import parse_date
from app.models.nft_athlete_card import MetaAthleteNFT
from app.models.file import File
from app.services.s3 import upload_file_to_s3

ALLOWED_IMAGE_EXTENSIONS = {'png', 'jpg', 'jpeg'}

parser = reqparse.RequestParser()
parser.add_argument('name', help='Name field required', required=True)
parser.add_argument('nft_uuid', help='Athlete NFT UUID', required=False)
parser.add_argument('kind', help='Kind field required', required=True)
parser.add_argument('sport', help='Sports field required', required=True)
parser.add_argument('birthdate', help='Birthdate field required', required=True)
parser.add_argument('weight', help='Weight field required', required=True)
parser.add_argument('height', help='Height field required', required=True)
parser.add_argument('schoolgrade', help='School Grade field required', required=True)
parser.add_argument('photo', type=FileStorage, location='files', help='Photo field required', required=True)
parser.add_argument('cardMinted', help='Cards Minted field required', required=False, type=inputs.boolean)
parser.add_argument('quantity_gold', help='Athlete gold quantity', type=inputs.positive, required=False)
parser.add_argument('quantity_platinum', help='Athlete platinum quantity', type=inputs.positive, required=False)
parser.add_argument('quantity_diamond', help='Athlete diamond quantity', type=inputs.positive, required=False)


def allowed_imagefile(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_IMAGE_EXTENSIONS


class MetaAlthleteAdd(MethodResource, Resource):
    @doc(description='This resource for this endpoint /nftathletecard_add for save data into database',
         version='1.0',
         tags=['Meta Athletes Primitive']
         )
    def post(self):
        try:
            data = parser.parse_args()
            birth_date = parse_date(data['birthdate'])

            kind = UserType.fetch_items(data['kind'])
            if not kind:
                return {'message': 'Invalid Kind Type'}, 400

            sport = SportType.fetch_items(data['sport'])
            if not sport:
                return {'message': 'Invalid Sport Type'}, 400

            schoolgrade = SchoolGrade.fetch_items(data['schoolgrade'])
            if not schoolgrade:
                return {'message': 'Invalid School grade Type'}, 400

            image_file_data = data['photo']
            if image_file_data == '':
                return {'message': 'Image File Not Found'}, 404
            if image_file_data and allowed_imagefile(image_file_data.filename):
                image_location_url = upload_file_to_s3(image_file_data, folder="althleteimages")

                new_uploaded_file = File(
                    file_url=image_location_url,
                )
                new_uploaded_file.save_to_db()
                image_data = File.to_json(new_uploaded_file)

                new_meta_athlete = MetaAthleteNFT(
                    name=data['name'],
                    nft_uuid=data['nft_uuid'],
                    kind=kind,
                    sport=sport,
                    birthdate=birth_date,
                    weight=data['weight'],
                    height=data['height'],
                    schoolgrade=schoolgrade,
                    photo=image_data["p_id"],
                    cardMinted=data['cardMinted'],
                    quantity_gold=data['quantity_gold'],
                    quantity_platinum=data['quantity_platinum'],
                    quantity_diamond=data['quantity_diamond'],
                )
                new_meta_athlete.save_to_db()
                jsonify_data = MetaAthleteNFT.to_json(new_meta_athlete)
                jsonify_data["photo_detail"] = image_data
                return jsonify_data

            else:
                return {'message': 'File Format Not Allowed'}, 422
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class AllMetaAthlete(MethodResource, Resource):
    """this resource for /nftathletecard endpoint by this url all data can view"""

    @doc(description=' This resource for /nftathletecard endpoint by this url all data can view ',
         version='1.0',
         tags=['Meta Athletes Primitive']
         )
    def get(self):
        try:
            return MetaAthleteNFT.return_all()
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500


class MetaAthleteBase(MethodResource, Resource):
    """this resource for /nftathletecard/<int:p_id> endpoint by this url classes data can update, delete, single data
    view """

    @doc(
        description='this resource for /nftathletecard/<int:p_id> endpoint by this url classes data can single data '
                    'view',
        version='1.0',
        tags=['Meta Athletes Primitive']
        )
    def get(self, p_id):
        try:
            get_data = MetaAthleteNFT.find_by_id(p_id)
            if get_data:
                jsonify_data = MetaAthleteNFT.to_json(get_data)
                jsonify_data["photo_detail"] = File.to_json(get_data.photoObj)
                return jsonify_data
            else:
                return {'message': 'Data not found'}, 400
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
