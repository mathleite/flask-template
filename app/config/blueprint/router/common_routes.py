from flask import Blueprint

common_routes = Blueprint('common_routes', __name__)


@common_routes.route('/')
def hello_world():
    return "<p>Hello, World!</p>"
