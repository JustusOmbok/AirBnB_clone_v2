#!/usr/bin/python3
"""Simple flask web app for displaying filters."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity
from models.place import Place


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb', methods=['GET'])
def hbnb():
    """Displays Airbnb filters."""
    all_states = list(storage.all(State).values())
    amenities = list(storage.all(Amenity).values())
    places = list(storage.all(Place).values())

    all_states.sort(key=lambda state: state.name)
    amenities.sort(key=lambda amenity: amenity.name)
    places.sort(key=lambda place: place.name)
    for state in all_states:
        state.cities.sort(key=lambda city: city.name)
    ctxt = {
            'states': all_states,
            'amenities': amenities,
            'places': places
    }
    return render_template('100-hbnb.html', **ctxt)


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the db after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
