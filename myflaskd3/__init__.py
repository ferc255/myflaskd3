"""
Simple flask application.
"""
from flask import Flask
from myflaskd3.graph_bp import GRAPH_BP


APP = Flask(__name__)


def main():
    APP.register_blueprint(GRAPH_BP)
    APP.run()
