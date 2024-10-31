from flask import Blueprint
from controllers.stock_controller import get_stock_items
from bson.json_util import dumps

stock_bp = Blueprint('stock', __name__)

@stock_bp.route('/api/stock', methods=['GET'])
def get_stock():
    stock_items = get_stock_items()
    return dumps(stock_items)