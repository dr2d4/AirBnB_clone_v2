#!/usr/bin/python3
'''
    Creta server and new route to index
'''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    '''Prints message Hello HBNB!'''
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    '''Prints message HBNB'''
    return "HBNB"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
