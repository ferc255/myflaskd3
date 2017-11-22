"""
Simple flask application.
"""
from flask import Flask
from myflaskd3.views import GRAPH_BP

APP = Flask(__name__)
APP.register_blueprint(GRAPH_BP)
