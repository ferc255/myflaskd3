"""
Simple flask application.
"""
from flask import Flask
APP = Flask(__name__)


@APP.route('/')
def sample_view():
    """
    Sample view.
    """

    return 'hello world!'
