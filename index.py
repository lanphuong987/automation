from flask import Flask, jsonify
from flask import render_template
from templates import *
app = Flask(__name__)


@app.route("/")
def index():
    return render_template('index.html')


@app.errorhandler(404)
def not_found_error(error):
    return render_template('page-404.html'), 404




if __name__ == "__main__":
    app.run()



