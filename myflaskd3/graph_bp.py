'''
Views for the application.
'''
import os
import json
import sqlite3
from flask import (
    Blueprint,
    jsonify,
    render_template,
    request,
    send_file,
)


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
GRAPH_BP = Blueprint('graph_bp', __name__, template_folder='templates',
                     static_folder='static')


@GRAPH_BP.route('/graph', methods=['GET', 'POST'])
def graph_view():
    """
    Service view for JS-handling.

    If Content-Type is equal to text/html then returns list
    of available graphs for drawing.

    If it is equal to application/json then returns
    selected graph, which is from json payload.
    """

    dbase = sqlite3.connect(os.path.join(BASE_DIR, 'database.db')).cursor()
    if request.headers['Content-Type'] == 'text/html':
        dbase.execute("SELECT name FROM Graph")
        select_result = dbase.fetchall()

        response = {'graphs': []}
        for item in select_result:
            response['graphs'].append(item[0])

        return jsonify(response)

    if request.headers['Content-Type'] == 'application/json':
        name = json.loads(request.get_data().decode())['name']
        dbase.execute("SELECT json FROM Graph "
                      "WHERE name = ?;",
                      (name, ))

        response = dbase.fetchall()[0][0]
        return jsonify(json.loads(response))

    return 'The Content-Type is not allowed for the requested URL'


@GRAPH_BP.route('/client')
def main_view():
    """
    Main view that contains the graph.
    """

    return render_template('graph_sample.html')


@GRAPH_BP.route('/static/<filepath>')
def static_view(filepath):
    """
    This view is used to provide access to static files.
    """

    return GRAPH_BP.send_static_file(filepath)


@GRAPH_BP.route('/media/<filepath>')
def media_view(filepath):
    """
    This view is used to provide access to media files.
    """

    return send_file(os.path.join(BASE_DIR,
                                  os.path.join(os.path.dirname(
                                      os.path.abspath(__file__)),
                                               os.path.join('media',
                                                            filepath))))
