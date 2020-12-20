import flask
from flask import request

app = flask.Flask(__name__)


@app.route('/', methods=['GET'])
def home():
    year = int(request.args['year'])
    return year

if __name__ == "__main__":
    app.run()