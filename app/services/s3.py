import os
import boto3
from werkzeug.utils import secure_filename
from ulid import ULID

from run import app

access_key = app.config['AWS_ACCESS_KEY']
secret_key = app.config['AWS_SECRET_ACCESS_KEY']
bucket = app.config['AWS_BUCKET_NAME']
endpoint_url = app.config['AWS_CLUSTER_LOCATION']
s3_url = app.config['AWS_S3_LOCATION']

s3 = boto3.client(
    "s3",
    aws_access_key_id=access_key,
    aws_secret_access_key=secret_key,
    endpoint_url=endpoint_url,
)

def upload_file_to_s3(file, folder=None, acl="public-read"):
    filename = f"{str(ULID())}." + secure_filename(file.filename).rsplit(".", 1)[1].lower()
    filename = f"{folder.strip('/')}/{filename}" if folder else filename

    try:
        s3.upload_fileobj(
            file,
            bucket,
            filename,
            ExtraArgs={
                "ACL": acl,
                "ContentType": file.content_type
            }
        )

    except Exception as e:
        print("Something Happened: ", e)
        return e

    return s3_url + filename