#!/usr/bin/python3
""" A flask web application.
"""
from flask import Flask

app = Flask(__name__)
"""Instance for flask app."""
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Hello HBNB is printed """
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
