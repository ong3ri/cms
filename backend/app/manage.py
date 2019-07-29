import click
import os

from sqlalchemy_utils.functions import (database_exists, create_database)


def init_commands(app):

    @app.cli.command()
    def init_db():
        """Creates database and models"""
        database_url = '{dialect}+{driver}://{user}:{password}@{host}:{port}/{dbname}' \
            .format(
                dialect='postgresql',
                driver='psycopg2',
                user=os.environ['S_RDS_USERNAME'],
                password=os.environ['S_RDS_PASSWORD'],
                host=os.environ['S_RDS_HOST'],
                port=os.environ['S_RDS_PORT'],
                dbname=os.environ['S_RDS_DB_NAME']
            )

        if database_exists(database_url):

            return click.echo("Database exists already!")
        else:
            click.echo("Creating database...")
            create_database(database_url)

            return click.echo("Database created.")
