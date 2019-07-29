import os


class Config(object):

    @staticmethod
    def init_app():
        pass


class ProductionConfigPsql(Config):
    SQLALCHEMY_DATABASE_URI = \
        '{dialect}+{driver}://{user}:{password}@{host}:{port}/{dbname}' \
        .format(
            dialect='postgresql',
            driver='psycopg2',
            user=os.environ['S_RDS_USERNAME'],
            password=os.environ['S_RDS_PASSWORD'],
            host=os.environ['S_RDS_HOST'],
            port=os.environ['S_RDS_PORT'],
            dbname=os.environ['S_RDS_DB_NAME']
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DevelopmentConfigPsql(Config):
    SQLALCHEMY_DATABASE_URI = \
        '{dialect}+{driver}://{user}:{password}@{host}:{port}/{dbname}'\
        .format(
            dialect='postgresql',
            driver='psycopg2',
            user=os.environ['S_RDS_USERNAME'],
            password=os.environ['S_RDS_PASSWORD'],
            host=os.environ['S_RDS_HOST'],
            port=os.environ['S_RDS_PORT'],
            dbname=os.environ['S_RDS_DB_NAME']
        )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


configuration = {
    'default': DevelopmentConfigPsql,
    'production': ProductionConfigPsql
}