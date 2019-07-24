from flask import Flask
import requests

app = Flask(__name__)


@app.route('/')
def index():
    return 'Main Index'


@app.route('/login', methods=['GET', 'POST'])
def login():
    if requests is 'POST':
        input('Enter your username: ')

    elif requests is 'GET':
        input('Enter login information: ')

    return login


