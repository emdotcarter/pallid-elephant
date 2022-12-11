from flask import Flask

app = Flask(__name__)


@app.route('/1/hello_world')
def hello_world():
    return '<h1>Hello, World!</h1>'
