"""
Auxiliary script which helps to fill database with some samples.
"""

import os
import json
import sqlite3

SOME_JSONS = [
    {
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
            {"source": "Computer_A1", "target": "Switch_1",
             "wire": "Straight"},
            {"source": "Computer_A2", "target": "Switch_1",
             "wire": "Straight"},
            {"source": "Computer_A3", "target": "Switch_1",
             "wire": "Straight"},
            {"source": "Switch_1", "target": "Router_1",
             "wire": "Straight"},
            {"source": "Computer_B1", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Computer_B2", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Computer_B3", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Computer_B4", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Switch_2", "target": "Router_2",
             "wire": "Straight"},
            {"source": "Computer_C1", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Computer_C2", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Computer_C3", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Switch_3", "target": "Router_3",
             "wire": "Straight"},
            {"source": "Router_1", "target": "Router_2",
             "wire": "Crossover"},
            {"source": "Router_1", "target": "Router_3",
             "wire": "Crossover"},
            {"source": "Router_2", "target": "Router_3",
             "wire": "Crossover"},
        ],
    },
    {
        "nodes": [
            {"name": "Computer_A1", "kind": "Host"},
            {"name": "Switch_1", "kind": "Switch"},
            {"name": "Computer_B1", "kind": "Host"},
            {"name": "Computer_B2", "kind": "Host"},
            {"name": "Switch_2", "kind": "Switch"},
            {"name": "Computer_C1", "kind": "Host"},
            {"name": "Computer_C2", "kind": "Host"},
            {"name": "Switch_3", "kind": "Switch"},

        {"name": "Computer_D1", "kind": "Host"},
            {"name": "Computer_D2", "kind": "Host"},
            {"name": "Computer_D3", "kind": "Host"},
            {"name": "Computer_D4", "kind": "Host"},
            {"name": "Computer_D5", "kind": "Host"},
        ],
        "links": [
            {"source": "Computer_A1", "target": "Switch_1",
             "wire": "Straight"},
            {"source": "Switch_1", "target": "Switch_2",
             "wire": "Crossover"},
            {"source": "Switch_1", "target": "Switch_3",
             "wire": "Crossover"},
            {"source": "Computer_B1", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Computer_B2", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Computer_C1", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Computer_C2", "target": "Switch_3",
             "wire": "Straight"},

            {"source": "Computer_D1", "target": "Computer_D2",
             "wire": "Crossover"},
            {"source": "Computer_D1", "target": "Computer_D3",
             "wire": "Crossover"},
            {"source": "Computer_D1", "target": "Computer_D4",
             "wire": "Crossover"},
            {"source": "Computer_D1", "target": "Computer_D5",
             "wire": "Crossover"},
            {"source": "Computer_D2", "target": "Computer_D3",
             "wire": "Crossover"},
            {"source": "Computer_D2", "target": "Computer_D4",
             "wire": "Crossover"},
            {"source": "Computer_D2", "target": "Computer_D5",
             "wire": "Crossover"},
            {"source": "Computer_D3", "target": "Computer_D4",
             "wire": "Crossover"},
            {"source": "Computer_D3", "target": "Computer_D5",
             "wire": "Crossover"},
            {"source": "Computer_D4", "target": "Computer_D5",
             "wire": "Crossover"},
        ],
    },
    {
        "nodes": [
            {"name": "Computer_A1", "kind": "Host"},
            {"name": "Computer_A2", "kind": "Host"},
            {"name": "Switch_1", "kind": "Switch"},
            {"name": "Router_1", "kind": "Router"},
            {"name": "Computer_B1", "kind": "Host"},
            {"name": "Computer_B2", "kind": "Host"},
            {"name": "Switch_2", "kind": "Switch"},

        {"name": "Computer_C1", "kind": "Host"},
            {"name": "Computer_C2", "kind": "Host"},
            {"name": "Computer_C3", "kind": "Host"},
            {"name": "Computer_C4", "kind": "Host"},
            {"name": "Computer_C5", "kind": "Host"},

        {"name": "Computer_D1", "kind": "Host"},
            {"name": "Computer_D2", "kind": "Host"},
            {"name": "Computer_D3", "kind": "Host"},
            {"name": "Computer_D4", "kind": "Host"},
            {"name": "Switch_3", "kind": "Switch"},
        ],
        "links": [
            {"source": "Computer_A1", "target": "Switch_1",
             "wire": "Straight"},
            {"source": "Computer_A2", "target": "Switch_1",
             "wire": "Straight"},
            {"source": "Switch_1", "target": "Router_1",
             "wire": "Straight"},
            {"source": "Computer_B1", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Computer_B2", "target": "Switch_2",
             "wire": "Straight"},
            {"source": "Switch_2", "target": "Router_1",
             "wire": "Straight"},
            
            {"source": "Computer_C1", "target": "Computer_C2",
             "wire": "Crossover"},
            {"source": "Computer_C2", "target": "Computer_C3",
             "wire": "Crossover"},
            {"source": "Computer_C3", "target": "Computer_C4",
             "wire": "Crossover"},
            {"source": "Computer_C4", "target": "Computer_C5",
             "wire": "Crossover"},
            {"source": "Computer_C5", "target": "Computer_C1",
             "wire": "Crossover"},

            {"source": "Computer_D1", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Computer_D2", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Computer_D3", "target": "Switch_3",
             "wire": "Straight"},
            {"source": "Computer_D4", "target": "Switch_3",
             "wire": "Straight"},
        ],
    },
]


if __name__ == '__main__':
    dbase = sqlite3.connect('../database.db')
    with dbase:
        cursor = dbase.cursor()
        try:
            cursor.execute("DROP TABLE Graph;")
        except sqlite3.OperationalError:
            pass
        
        try:
            cursor.execute("CREATE TABLE Graph (name TEXT, json TEXT);")
        except sqlite3.OperationalError:
            pass
   

        for i, item in enumerate(SOME_JSONS):
            cursor.execute("insert into Graph (name, json) values"
                           "(?, ?);",
                           ('example_' + str(i + 1), json.dumps(item)))
