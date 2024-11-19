from flask import Blueprint
from controllers.stock_controller import get_stock_items
from bson.json_util import dumps
from auth.auth_decorator import require_auth

stock_bp = Blueprint("stock", __name__)


@stock_bp.route("/api/stock", methods=["GET"])
@require_auth
def get_stock():
    stock_items = get_stock_items()
    return dumps(stock_items)
