#!/usr/bin/python3
"""

This script starts a Flask web application with the following routes:
1. Root route (/): Displays the message "Hello HBNB!"
2. /hbnb route: Displays the message "HBNB"
3. /c/<text> route: Displays "C " followed by the value of the text variable,
   replacing underscores (_) with spaces.
4. /python/(<text>) route: Displays "Python " followed by the value of the text variable,
   replacing underscores (_) with spaces. The default value of text is "is cool".
5. /number/<n> route: Displays "n is a number" only if n is an integer.
6. /number_template/<n> route: Displays an HTML page with an H1 tag containing "Number: n"
   only if n is an integer.
7. /number_odd_or_even/<n> route: Displays an HTML page with an H1 tag indicating whether
   "Number: n is even|odd" only if n is an integer.

"""

from flask import Flask, render_template, abort

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
    return 'C {}'.format(text.replace('_', ' '))


@app.route('/python/', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text='is cool'):
    """
    Route function for the /python/(<text>) endpoint.

    Args:
        text (str): The text parameter from the URL (default is 'is cool').

    Returns:
        str: The message "Python " followed by the value of the text variable,
             with underscores replaced by spaces.
    """
    return 'Python {}'.format(text.replace('_', ' '))


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    """
    Route function for the /number/<n> endpoint.

    Args:
        n (int): The integer parameter from the URL.

    Returns:
        str: The message "<n> is a number" if n is an integer, else a 404 error.
    """
    if isinstance(n, int):
        return '{} is a number'.format(n)
    else:
        abort(404)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    """
    Route function for the /number_template/<n> endpoint.

    Args:
        n (int): The integer parameter from the URL.

    Returns:
        HTML: An HTML page with an H1 tag containing "Number: n" if n is an integer.
    """
    if isinstance(n, int):
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def number_odd_or_even_route(n):
    """
    Route function for the /number_odd_or_even/<n> endpoint.

    Args:
        n (int): The integer parameter from the URL.

    Returns:
        HTML: An HTML page with an H1 tag indicating whether "Number: n is even|odd"
               if n is an integer.
    """
    if isinstance(n, int):
        return render_template('6-number_odd_or_even.html', n=n, result='even' if n % 2 == 0 else 'odd')
    else:
        abort(404)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
