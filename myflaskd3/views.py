'''
Views for the application.
'''

import os
import json
import sqlite3
from flask import render_template, send_file, jsonify, request

from myflaskd3 import APP

BASE_DIR = os.path.dirname(__file__)


@APP.route('/graph', methods=['GET', 'POST'])
def graph_view():
    '''
    Service view for JS-handling.
    Returns a list of available graphs for drawing.
    '''

    dbase = sqlite3.connect('database.db').cursor()
    if request.headers['Content-Type'] == 'text/html':
        dbase.execute("SELECT name FROM Graph")
        select_result = dbase.fetchall()

        response = {'graphs': []}
        for item in select_result:
            response['graphs'].append(item[0])

        return jsonify(response)
    elif request.headers['Content-Type'] == 'application/json':
        name = json.loads(request.get_data().decode())['name']
        dbase.execute("SELECT json FROM Graph "
                      "WHERE name = ?;",
                      (name, ))

        response = dbase.fetchall()[0][0]
        return jsonify(json.loads(response))
    else:
        return 'The Content-Type is not allowed for the requested URL'


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
