from flask import Blueprint

site = Blueprint('site', __name__)

@site.route('/')
def index():
    return "helooo"


@site.route("/welcome")
def welcome_msg():
    return "welcome to our app"