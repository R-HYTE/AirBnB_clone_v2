#!/usr/bin/python3
"""
This script starts a Flask web application with three routes:
1. Root route (/): Displays the message "Hello HBNB!"
2. /hbnb route: Displays the message "HBNB"
3. /c/<text> route: Displays "C " followed by the value of the text variable,
   replacing underscores (_) with spaces.

escape() ensures that the user-provided text is properly escaped
for HTML rendering, making the application more secure
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
        str: The message "C " followed by the value of the text variable.
    """
    return 'C {}'.format(escape(text.replace('_', ' ')))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)