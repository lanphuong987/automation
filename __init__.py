from flask import Flask, Blueprint
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.secret_key = "Fw\xc6\xab\x1bM\x82\xe1$\xf08\x91js\x92\x9d"
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:Phuong123%@localhost/automation?charset=utf8'

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

db = SQLAlchemy(app=app)

