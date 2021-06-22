from logging import debug
from flask import Flask

from .api.routes import api
from .site.routes import site
from .company.route import company

def create_app():
    app = Flask(__name__)

    app.register_blueprint(api)
    app.register_blueprint(site)
    app.register_blueprint(company)


    return app

