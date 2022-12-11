from sqlalchemy import engine_from_config
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

from config.config import DevConfig

app = Flask(__name__)
app.config.from_object('config.config.DevConfig')

db = SQLAlchemy(app)

@app.route('/1/hello_world')
def hello_world():
    return '<h1>Hello, World!</h1>'
