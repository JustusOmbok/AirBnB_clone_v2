#!/usr/bin/python3
""" Simple flask web app to display states and their cities."""

from models import storage
from flask import Flask, render_template
from models.state import State
from models.city import City


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/states', methods=['GET'])
@app.route('/states/<state_id>', methods=['GET'])
def states(state_id=None):
    """Displays states and their cities"""
    states = storage.all("State")
    if state_id is not None:
        state_id = 'state.' + state_id
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes database at end of request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
