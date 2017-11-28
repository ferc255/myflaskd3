"""
Simple flask application.
"""

from flask import Flask
from myflaskd3.graph_bp import GRAPH_BP


APP = Flask(__name__)


def register_blueprints():
    '''
    Blueprints registration
    '''

    APP.register_blueprint(GRAPH_BP)


def main():
    """
    The main function which runs server.
    """

    register_blueprints()
    APP.run(debug=True)
