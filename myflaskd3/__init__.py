"""
Simple flask application.
"""
from flask import Flask
from myflaskd3.graph_bp import GRAPH_BP


APP = Flask(__name__)
APP.register_blueprint(GRAPH_BP)    


def main():
    """
    The main function which runs server.
    """
    
    APP.run()
