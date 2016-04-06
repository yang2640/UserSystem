from flask import Blueprint

# create the blueprint to be registered in the app __init__.py
main = Blueprint('main', __name__)

# import views and erros
from . import views, errors