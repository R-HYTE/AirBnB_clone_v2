#!/usr/bin/python3
"""
This script starts a Flask web application with a route
that displays "Hello HBNB!"
The application listens on 0.0.0.0, port 5000,
and uses the option strict_slashes=False.
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


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
