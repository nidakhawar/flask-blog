# import Flask class from the flask module
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
# create a new instance of Flask and store it in app 
app = Flask(__name__)
db=SQLAlchemy(app)
app.config['SECRET_KEY'] = getenv('SECRET_KEY')
app.config['SQLALCHEMY_DATABASE_URI'] = getenv('DATABASE_URI')
# import the ./application/routes.py file
from application import routes