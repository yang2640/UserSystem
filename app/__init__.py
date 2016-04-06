from flask import Flask
from flask.ext.bootstrap import Bootstrap
from flask.ext.mail import Mail
from flask.ext.moment import Moment
from flask.ext.sqlalchemy import SQLAlchemy
from config import config

# create bootstrap
bootstrap = Bootstrap()
# create mail
mail = Mail()
# create moment
moment = Moment()
# create db
db = SQLAlchemy()


# this function is called in manage.py, pass in the config name
def create_app(config_name):
    app = Flask(__name__)
    # get config from the Config class
    app.config.from_object(config[config_name])
    # call the config init method
    config[config_name].init_app(app)

    # other init methods
    bootstrap.init_app(app)
    mail.init_app(app)
    moment.init_app(app)
    db.init_app(app)

    from .main import main as main_blueprint
    # register the blue print
    app.register_blueprint(main_blueprint)

    return app