from flask import Flask, render_template, make_response, jsonify
from quotes import get_quote

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/quote")
def quote():
    quote = get_quote()
    return make_response(jsonify(quote), 200)