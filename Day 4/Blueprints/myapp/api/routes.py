from flask import Blueprint

#api = Blueprint('api', __name__, url_prefix='/api')
api = Blueprint('api', __name__)

@api.route('/sample')
def sample():
    return {"name": "venkat", "age": 24}