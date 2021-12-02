# Create the flask object
from flask import *

from flask import Flask, render_template, session, flash, redirect, url_for

app = Flask(__name__)  # __name__ means main


@app.route('/')
def home():
    return render_template ('index.html')


@app.route('/projects')
def projects():
    return render_template('projects.html')


@app.route('/aboutme')
def aboutme():
    return render_template('aboutme.html')

@app.route('/contactme')
def contact():
    return render_template('contactme.html')


# check
if __name__ == '__main__':
    app.run(debug=True)
