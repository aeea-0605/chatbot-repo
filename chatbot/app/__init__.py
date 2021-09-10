from flask import *
from flask.app import Flask
from app.config import Config

app = Flask(__name__)
app.config.from_object(Config)

from app.routes import bot