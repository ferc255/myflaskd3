'''
Views for the application.
'''

import os
import json
from flask import render_template, send_file

from myflaskd3 import APP

BASE_DIR = os.path.dirname(__file__)
SOME_JSON = {
    "nodes": [
        {"name": "Computer_A1", "kind": "Host"},
        {"name": "Computer_A2", "kind": "Host"},
        {"name": "Computer_A3", "kind": "Host"},
        {"name": "Switch_1", "kind": "Switch"},
        {"name": "Router_1", "kind": "Router"},
        {"name": "Computer_B1", "kind": "Host"},
        {"name": "Computer_B2", "kind": "Host"},
        {"name": "Computer_B3", "kind": "Host"},
        {"name": "Computer_B4", "kind": "Host"},
        {"name": "Switch_2", "kind": "Switch"},
        {"name": "Router_2", "kind": "Router"},
        {"name": "Computer_C1", "kind": "Host"},
        {"name": "Computer_C2", "kind": "Host"},
        {"name": "Computer_C3", "kind": "Host"},
        {"name": "Switch_3", "kind": "Switch"},
        {"name": "Router_3", "kind": "Router"},

        {"name": "Computer_D1", "kind": "Host"},
        {"name": "Computer_D2", "kind": "Host"},
        {"name": "Switch_4", "kind": "Switch"},
        {"name": "Router_4", "kind": "Router"},
        {"name": "Computer_E1", "kind": "Host"},
        {"name": "Computer_E2", "kind": "Host"},
        {"name": "Switch_5", "kind": "Switch"},
    ],
    "links": [
        {"source": "Computer_A1", "target": "Switch_1", "wire": "Straight"},
        {"source": "Computer_A2", "target": "Switch_1", "wire": "Straight"},
        {"source": "Computer_A3", "target": "Switch_1", "wire": "Straight"},
        {"source": "Switch_1", "target": "Router_1", "wire": "Straight"},
        {"source": "Computer_B1", "target": "Switch_2", "wire": "Straight"},
        {"source": "Computer_B2", "target": "Switch_2", "wire": "Straight"},
        {"source": "Computer_B3", "target": "Switch_2", "wire": "Straight"},
        {"source": "Computer_B4", "target": "Switch_2", "wire": "Straight"},
        {"source": "Switch_2", "target": "Router_2", "wire": "Straight"},
        {"source": "Computer_C1", "target": "Switch_3", "wire": "Straight"},
        {"source": "Computer_C2", "target": "Switch_3", "wire": "Straight"},
        {"source": "Computer_C3", "target": "Switch_3", "wire": "Straight"},
        {"source": "Switch_3", "target": "Router_3", "wire": "Straight"},
        {"source": "Router_1", "target": "Router_2", "wire": "Crossover"},
        {"source": "Router_1", "target": "Router_3", "wire": "Crossover"},
        {"source": "Router_2", "target": "Router_3", "wire": "Crossover"},

        {"source": "Computer_D1", "target": "Switch_4", "wire": "Straight"},
        {"source": "Computer_D2", "target": "Switch_4", "wire": "Straight"},
        {"source": "Switch_4", "target": "Router_4", "wire": "Straight"},
        {"source": "Computer_E1", "target": "Switch_5", "wire": "Straight"},
        {"source": "Computer_E2", "target": "Switch_5", "wire": "Straight"},
        {"source": "Switch_5", "target": "Router_4", "wire": "Straight"},
    ],
}


@APP.route('/')
def main_view():
    """
    Main view that contains the graph.
    """

    return render_template('graph_sample.html', myjson2=json.dumps(SOME_JSON))


@APP.route('/static/<filepath>')
def static_view(filepath):
    '''
    This view is used to provide access to static files.
    '''

    return APP.send_static_file(filepath)


@APP.route('/media/<filepath>')
def media_view(filepath):
    '''
    This view is used to provide access to media files.
    '''

    return send_file(os.path.join(
        os.path.join(BASE_DIR, 'media'), filepath))
