#!/usr/bin/python3
"""Flask web application to show states and specific state details"""

from flask import Flask, render_template
from models import storage

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<state_id>', strict_slashes=False)
def states_and_specific_state(state_id=None):
    """Render states and specific state details"""
    states = storage.all("State")
    return render_template('9-states.html', states=states, state_id=state_id)


@app.teardown_appcontext
def close_storage_session(error):
    """Ensure storage is closed after each request"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
