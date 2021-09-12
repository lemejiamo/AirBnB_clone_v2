#!/usr/bin/python3
""" Module to mange flask Server"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ return index"""
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """" return HBNB"""
    return 'HBNB'


@app.route('/c/<string_p>')
def c_is_fun(string_p):
    """ print args get it for url"""

    string = string_p.split("_")
    new_string = ""
    for word in string:
        new_string = new_string + " " + word
    return new_string[1:]


@app.route('/python')
@app.route('/python/')
def default_phyton():
    """ default_phyton """
    return ("Python is cool")


@app.route('/python/<text>')
def python_route(text):
    """ python Route """
    string = c_is_fun(text)
    print(string)
    return ("Python {}".format(string))


@app.route('/number/<n>')
def number_route(n):
    """ number route """
    if '.' not in n:
        return n + " " + "is a number"
    pass


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
