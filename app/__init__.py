from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)

app.config.from_object('config')




db = SQLAlchemy(app)
migrate = Migrate(app, db)


from app.controllers import routes

from app.models import filme
from app.models import usuario
from app.models import aluguel


