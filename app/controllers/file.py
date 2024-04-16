import os
from flask_restful import Resource, reqparse
from flask_jwt_extended import jwt_required
from werkzeug.datastructures import FileStorage  
from werkzeug.utils import secure_filename
from flask_apispec import marshal_with, doc, use_kwargs
from flask_apispec.views import MethodResource
from marshmallow import Schema, fields
from run import app
from app.models.file import File
from app.services.s3 import upload_file_to_s3


ALLOWED_EXTENSIONS = {'parquet', 'json', 'csv', 'png', 'jpg', 'jpeg'}  

parser = reqparse.RequestParser()
parser.add_argument('file', type=FileStorage, location='files', help='File field required', required=True)
parser.add_argument('folder', help='Folder to be uploaded')


class FileResponseSchema(Schema):
    file_url = fields.Str(default='None')


class FileRequestSchema(Schema):
    file = fields.String(required=True, description="File Upload field is required")
    folder = fields.String(required=False, description="Folder to upload the file")


class UploadFile(MethodResource, Resource):
    """ this resource for this endpoint /uploadfile for save data into database"""

    def allowed_file(self,filename):
        return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

    @doc(description='This resource for this endpoint /uploadfile for save upload files into database',
        version='1.0',
        tags=['Upload Files']
    )
    def post(self): 
        try:
            data = parser.parse_args()
            file_data = data['file']
            folder_data = data['folder']

            if file_data == '':
                return {'message': 'File Not Found'}, 404

            if file_data and self.allowed_file(file_data.filename):                
                location_url = upload_file_to_s3(file_data, folder=folder_data)

                new_uploaded_file = File(
                    file_url   = location_url,
                )
                new_uploaded_file.save_to_db()

                jsonify_data = File.to_json(new_uploaded_file)
                return jsonify_data

            else:
                return {'message': 'File Format Not Allowed'}, 422
        except Exception as e:
            print(e)
            return {'message': 'Something went wrong'}, 500
