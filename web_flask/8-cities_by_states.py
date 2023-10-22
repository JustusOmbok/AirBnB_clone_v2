#!/usr/bin/python3
""" Simple flask web app to display states and their cities."""

from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/cities_by_states')
def cities_by_states():
    """Displays a list of states and their cities."""
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def teardown_db(exception):
    """ Closes database at end of request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
