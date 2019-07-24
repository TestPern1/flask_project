from flask import (
    Flask,
    render_template
)
import requests

app = Flask(__name__, template_folder='templates')


@app.route('/')
def home():
    return render_template('home.html')


@app.route('/web')
def call():
    call = requests.get('https://finance.yahoo.com/portfolios')
    jsonify = call.text
    return jsonify


if __name__ == '__main__':
    app.run(debug=True)
