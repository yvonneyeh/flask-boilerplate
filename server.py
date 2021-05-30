from flask import Flask
from model import connect_to_db
import os

app = Flask(__name__)


@app.route('/')
def hello():
    return 'Hello, World!'