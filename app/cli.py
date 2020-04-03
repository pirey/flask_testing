import os
from app.db import session, reset_db


def init_app(app):
    @app.cli.command('reset-db', short_help="Clear database, then init database.")
    def reset_db_command():
        from . import models

        try:
            reset_db()
            print('ok')
        except Exception as e:
            print(e)
            print('not ok')

    @app.cli.command('generate-key', short_help="Generate secret key.")
    def generate_key():
        print(os.urandom(16))

    return app
