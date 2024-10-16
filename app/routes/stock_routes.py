from flask import Blueprint

stock_routes_bp = Blueprint('stock_routes_bp', __name__)

@stock_routes_bp.route('/')
def index():
    return 'Hello, World!'