#!/usr/bin/python3
'''
    Creta server and new route to index
'''

from flask import render_template
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


@app.route('/c/<text>', strict_slashes=False)
def text(text):
    '''Print passed text'''
    spaced_text = text.replace('_', ' ')
    return 'C {}'.format(spaced_text)


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text="is cool"):
    '''Print python + passed text'''
    spaced_text = text.replace('_', ' ')
    return 'Python {}'.format(spaced_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_n(n):
    '''Print a number passed in request'''
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def html_display_num(n):
    '''Send context to the template and rendering'''
    return render_template('5-number.html', n=n)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
