#!/usr/bin/python3
"""Simple flask web app for displaying filters."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters', methods=['GET'])
def hbnb_filters():
    """Displays Airbnb filters."""
    states = sorted(storage.all(State).values(), key=lambda state: state.name)
    cities = sorted(storage.all(City).values(), key=lambda city: city.name)
    amenities = sorted(storage.all(Amenity).values(),
                       key=lambda amenity: amenity.name)
    return render_template(
            '10-hbnb_filters.html',
            states=states,
            cities=cities,
            amenities=amenities
            )


@app.teardown_appcontext
def teardown_db(exception):
    """Closes the db after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
