#!/usr/bin/python3
"""
This script starts a Flask web application with two routes:
1. Root route (/): Displays the message "Hello HBNB!"
2. /hbnb route: Displays the message "HBNB"
"""

from flask import Flask

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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

