#!/usr/bin/python3
"""Flask web application to display states and cities"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states_and_cities', strict_slashes=False)
def states_and_cities_list():
    """Renders a list of states and their cities."""
    all_states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=all_states)


@app.teardown_appcontext
def close_storage(exc):
    """Closes the storage after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
