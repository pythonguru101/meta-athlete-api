from decouple import config


class Config(object):
    DEBUG = True
    TESTING = False
    SQLALCHEMY_DATABASE_URI = f"postgresql://{config('POSTGRES_USER')}:{config('POSTGRES_PASSWORD')}@{config('DB_HOST')}/{config('POSTGRES_DB')}"
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = config('SECRET_KEY')
    JWT_SECRET_KEY = config('JWT_SECRET_KEY')
    AWS_BUCKET_NAME = config('AWS_BUCKET_NAME')
    AWS_ACCESS_KEY = config('AWS_ACCESS_KEY')
    AWS_SECRET_ACCESS_KEY = config('AWS_SECRET_ACCESS_KEY')
    AWS_CLUSTER_LOCATION = config('AWS_CLUSTER_LOCATION')
    AWS_S3_LOCATION = config('AWS_S3_LOCATION')

class DevelopmentConfig(Config):
    DEBUG = True


class ProductionConfig(Config):
    DEBUG = False
