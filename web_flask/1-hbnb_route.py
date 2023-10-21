#!/usr/bin/python3
""" Flask wed app with routes.
"""
from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Display "Hello HBNB!" at the root.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Displays "HBNB" at the /hbnb route.
    """
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
