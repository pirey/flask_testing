import os

from datetime import datetime
from flask import Flask, request, jsonify

from app.logger import logger
from app.db import session
from app import schemas, models, cli

app = Flask(__name__)
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

cli.init_app(app)

@app.teardown_appcontext
def shutdown_session(exception=None):
    session.remove()


@app.route('/')
def index():
    return 'It works'

@app.route('/items/', methods=['GET'])
def get_items():
    items = models.Item.query.all()
    return jsonify(schemas.ItemSchema().dump(items, many=True))

