from flask import Flask, request, redirect, render_template, session, flash
import re

from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "supersecret"

mysql = MySQLConnector(app, 'users')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register')
def register():
    """Validate and hash registration data."""
    # first name - letters only, 2+ chars min
    # last name - letters only, 2+ chars min
    # email - valid email format
    # password - 8 char minimum, apply md5 hash
    # password confirmaiton must match password.
    # Flash error if registration fails
    pass


@app.route('/login')
def login():
    # verify that email and password match a user
    # Save matching user's id to session.
    # Flash error if login fails
    pass
