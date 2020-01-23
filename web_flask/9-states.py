#!/usr/bin/python3
'''
    Creta server and new route to index
'''

from flask import render_template
from models.state import State
from models import storage
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


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def tells_even_or_odd(n):
    '''Check if int passed is odd or even'''
    is_oe = ['is ', 'odd']

    if not n % 2:
        is_oe[1] = 'even'

    return render_template('6-number_odd_or_even.html', n=n, oe=''.join(is_oe))


@app.route('/states_list', strict_slashes=False)
def states_list_html():
    ''' Print all states '''
    state_objs = storage.all(eval('State'))
    state_values = []

    for key, value in state_objs.items():
        state_values.append(value)

    return render_template('7-states_list.html', states=state_values)


@app.route('/cities_by_states', strict_slashes=False)
def cities_states_list_html():
    ''' Print all cities by state '''
    state_objs = storage.all(eval('State'))
    state_values = []

    for key, value in state_objs.items():
        state_values.append(value)

    return render_template('8-cities_by_states.html', states=state_values)


@app.route('/states/', strict_slashes=False)
@app.route('/states/<id_state>', strict_slashes=False)
def state_id(id_state=None):
    ''' Print all cities by state '''
    state_objs = storage.all(eval('State'))
    state_values = []
    obj = None

    if id_state:
        obj = state_objs.get('State.{}'.format(id_state))
        obj = obj if obj else -1

    for key, value in state_objs.items():
        state_values.append(value)

    return render_template('9-states.html', states=state_values, obj=obj)


@app.teardown_appcontext
def session_closer(session):
    ''' Close session '''
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
