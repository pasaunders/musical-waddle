from flask import Flask, request, redirect, render_template, session, flash
import re

from mysqlconnection import MySQLConnector
app = Flask(__name__)
app.secret_key = "supersecret"
EMAIL_REGEX = re.compile(r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')


mysql = MySQLConnector(app, 'users')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/register', methods=['POST'])
def register():
    """Validate and hash registration data."""
    # first name - letters only, 2+ chars min
    # last name - letters only, 2+ chars min
    # email - valid email format
    # password - 8 char minimum, apply md5 hash
    # password confirmaiton must match password.
    # Flash error if registration fails
    pass


@app.route('/login', methods=['POST'])
def login():
    # verify that email and password match a user
    # Save matching user's id to session.
    # Flash error if login fails
    pass
