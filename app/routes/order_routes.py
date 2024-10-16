from flask import Blueprint, jsonify, request
from services import order_service
from bson.json_util import dumps

order_bp = Blueprint('order', __name__)

@order_bp.route('/api/order', methods=['GET'])
def get_order():
    order_items = order_service.get_order_items()
    return dumps(order_items)

@order_bp.route('/api/order/<order_number>', methods=['GET'])
def get_order_by_number(order_number):
    order = order_service.get_order_by_number(order_number) 
    return dumps(order)

@order_bp.route('/api/order' , methods=['POST'])
def create_order():
    order = request.json
    order_id = order_service.insert_order(order)
    return jsonify({'order_id': order_id})