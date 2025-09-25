from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SECRET_KEY'] = 'aHJCOz/~9$[L6:A1£&n,bA|8Q(#Q~@~_'

db = SQLAlchemy(app)
migrate = Migrate(app, db)

from mod.routes import home
from mod.models import Tarefas