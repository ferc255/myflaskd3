'''
Views for the application.
'''

import os
import json
import sqlite3
from flask import render_template, send_file, jsonify

from myflaskd3 import APP

BASE_DIR = os.path.dirname(__file__)


@APP.route('/graph')
def graph_view():
    '''
    Service view for JS-handling.
    Returns a list of available graphs for drawing.
    '''

    dbase = sqlite3.connect('database.db').cursor()
    dbase.execute("select name from Graph")
    arr = dbase.fetchall()

    response = {'graphs': []}
    for item in arr:
        response['graphs'].append(item[0])

    return jsonify(response)


@APP.route('/graph/<name>')
def send_graph(name):
    '''
    Service view for JS-handling.
    Returns a graph in a json format.
    '''

    dbase = sqlite3.connect('database.db').cursor()
    dbase.execute("SELECT json FROM Graph "
                  "WHERE name = ?;",
                  (name, ))

    response = dbase.fetchall()[0][0]
    return jsonify(json.loads(response))


@APP.route('/client')
def main_view():
    """
    Main view that contains the graph.
    """

    return render_template('graph_sample.html')


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
