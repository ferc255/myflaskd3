"""
Simple flask application.
"""

import os
import json
from flask import Flask, render_template, send_file

APP = Flask(__name__)
SOME_JSON = {
    "nodes": [
        {"name": "Computer_A1", "kind": "Host"},
        {"name": "Computer_A2", "kind": "Host"},
        {"name": "Switch_1", "kind": "Switch"},
        {"name": "Router_1", "kind": "Router"},
        {"name": "Switch_2", "kind": "Switch"},
        {"name": "Computer_B1", "kind": "Host"},
        {"name": "Computer_B2", "kind": "Host"},
    ],
    "links": [
        {"source": "Computer_A1", "target": "Switch_1", "wire": "Straight"},
        {"source": "Computer_A2", "target": "Switch_1", "wire": "Straight"},
        {"source": "Switch_1", "target": "Router_1", "wire": "Straight"},
        {"source": "Computer_B1", "target": "Switch_2", "wire": "Straight"},
        {"source": "Computer_B2", "target": "Switch_2", "wire": "Straight"},
        {"source": "Switch_2", "target": "Router_1", "wire": "Straight"},
    ],
}


@APP.route('/')
def sample_view():
    """
    Sample view.
    """

    return render_template('graph_sample.html', myjson2=json.dumps(SOME_JSON))


@APP.route('/static/<filepath>')
def static_view(filepath):
    '''
    Static view.
    '''

    return APP.send_static_file(filepath)


@APP.route('/media/<filepath>')
def media_view(filepath):
    '''
    Media view.
    '''

    return send_file(os.path.join(
        os.path.join(os.getcwd(), 'media'), filepath))
