#!/usr/bin/python3
""" Flask web app with routes.
"""
from flask import Flask, render_template


app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """ Displays "Hello HBNB" at the root.
    """
    return "Hello HBNB!"


@app.route('/hbnb')
def hbnb():
    """ Displays "HBNB" at /hbnb route.
    """
    return "HBNB"


@app.route('/c/<text>')
def c_route(text):
    """ Displays "C " followed by the value of the text.
    """
    return "C " + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def python_route(text="is cool"):
    """ Displays Python followed by the value of the text.
    """
    return "Python " + text.replace("_", " ")


@app.route('/number/<int:n>')
def number_route(n):
    """ Displays "n is a number" only if n is an integer.
    """
    return "{} is a number".format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """ Display an HTML page with a H1 tag'
    """
    return render_template('5-number.html', number=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """ Displays a HTML page with a h1 tag.
    """
    if n % 2 == 0:
        odd_or_even = "even"
    else:
        odd_or_even = "odd"
    return render_template('6-number_odd_or_even.html', 
            number=n, 
            odd_or_even=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
