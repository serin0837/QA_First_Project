from flask import Flask
from flask_sqlalchemy import SQLAlchemy
import os
import pymysql

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['QA_DATABASE_CONNECTION']
#app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
