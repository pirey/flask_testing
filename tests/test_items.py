import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.realpath(
    os.path.dirname(__file__)), '.env.testing')
load_dotenv(dotenv_path)

from app import app
from app.db import reset_db

def test_index(client):
    response = 'it works'
    reset_db()
    client = app.test_client()
    response = client.get('/').get_json()
    assert response == 'it works'
