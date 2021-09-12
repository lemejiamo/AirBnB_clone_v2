#!/usr/bin/python3
""" Module to mange flask Server"""


from flask import Flask


app = Flask(__name__)


@app.route('/', strict_slashes=False)
def index():
    """ route to root """
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """" route to HBNB"""
    return 'HBNB'


@app.route('/c/<string_p>')
def c_is_fun(string_p):
    """ print args get it for url"""
    string = string_p.split("_")
    new_string = ""
    for word in string:
        new_string = new_string + " " + word
    return new_string[1:]


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
