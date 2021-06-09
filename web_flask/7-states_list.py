#!/usr/bin/python3
""" Module comment """

from flask import Flask
from models import storage
from models.state import State
from flask import render_template

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def closetorage(self):
    """Close storage session"""
    storage.close()


@app.route('/states_list')
def trace_route():
    """ Display states in HTML"""
    states = storage.all(State).values()
    return render_template('7-states_list.html', states=states)


if __name__ == "__main__":
    app.run(port=5000, host='0.0.0.0', debug=True)