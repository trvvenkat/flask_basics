from flask import Blueprint

company = Blueprint('company', __name__)


@company.route("/getcompany")
def getcomp():
    return "JFH - Company name"