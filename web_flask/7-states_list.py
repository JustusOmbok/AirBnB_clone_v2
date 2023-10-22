#!/usr/bin/python3
""" A simple flask web app.
"""

from models import storage
from flask import Flask, render_template
from models.state import State


app = Flask(__name__)
""" Flasks' app instance."""
app.url_map.strict_slashes = False


@app.route('/states_list')
def states_list():
    """ Page for states_list."""
    all_states = list(storage.all(State).values())
    all_states.sort(key=lambda x: x.name)
    ctxt = {
            'states': all_states
    }
    return render_template('7-states_list.html', **ctxt)


@app.teardown_appcontext
def flask_teardown(exc):
    """ Event listener ends with this request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
