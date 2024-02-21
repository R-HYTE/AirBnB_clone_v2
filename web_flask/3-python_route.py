#!/usr/bin/python3
"""

This script starts a Flask web application with four routes:
1. Root route (/): Displays the message "Hello HBNB!"
2. /hbnb route: Displays the message "HBNB"
3. /c/<text> route: Displays "C " followed by the value of the text variable,
   replacing underscores (_) with spaces.
4. /python/<text> route: Displays "Python " followed by
    the value of the text variable, replacing underscores (_) with spaces.
    The default value of text is "is cool".


When you use Flask's templating engine or return HTML in your routes,
Flask will take care of escaping special characters to prevent them
from being interpreted as HTML or JavaScript

"""
from flask import Flask
from werkzeug.utils import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    Route function for the root endpoint.

    Returns:
        str: A simple greeting message.
    """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Route function for the /hbnb endpoint.

    Returns:
        str: The message "HBNB".
    """
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    """
    Route function for the /c/<text> endpoint.

    Args:
        text (str): The text parameter from the URL.

    Returns:
        str: The message "C " followed by the value of the text variable,
             with underscores replaced by spaces.
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))


@app.route('/python/')
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Route function for the /python/<text> endpoint.

    Args:
        text (str): The text parameter from the URL (default is 'is cool').

    Returns:
        str: The message "Python " followed by the value of the text variable,
             with underscores replaced by spaces.
    """
    return 'Python {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
