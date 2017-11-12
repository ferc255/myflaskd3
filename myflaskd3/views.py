'''
Views for the application.
'''

import os
import json
import sqlite3
from flask import render_template, send_file, jsonify

from myflaskd3 import APP

BASE_DIR = os.path.dirname(__file__)
SOME_JSON1 = {
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

SOME_JSON2 = {
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
    ],
}

@APP.route('/trash')
def client_view():
    conn = sqlite3.connect('database.db')
    #conn.execute("create table student ("
    #             "name TEXT, city TEXT)")

    ss1 = json.dumps(SOME_JSON1)
    ss2 = json.dumps(SOME_JSON2)
    conn.cursor().execute("insert into Graph (name, json) values"
                          "('ss1', ?);",
                          (ss1,) )
    conn.cursor().execute("insert into Graph (name, json) values"
                          "('ss2', ?);",
                          (ss2,) )
    conn.commit()
    conn.close()
    return 'hello'


@APP.route('/graph')
def graph_view():
    conn = sqlite3.connect('database.db').cursor()

    conn.execute("select name from Graph")

    arr = conn.fetchall();
    
    response = {'graphs': []}
    for item in arr:
        response['graphs'].append(item[0])

    print(response)
    
    return jsonify(response)


@APP.route('/graph/<name>')
def send_graph(name):
    print(name)
    db = sqlite3.connect('database.db').cursor()
    db.execute("SELECT json FROM Graph "
               "WHERE name = ?;",
               (name, ) )

    response = db.fetchall()[0][0];
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
