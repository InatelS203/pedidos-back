from flask import Blueprint, jsonify, request
from controllers import order_controller
from bson.json_util import dumps

order_bp = Blueprint('order', __name__)

@order_bp.route('/api/order', methods=['GET'])
def get_order():
    order_items = order_controller.get_order_items()
    return dumps(order_items)

@order_bp.route('/api/order/<order_number>', methods=['GET'])
def get_order_by_number(order_number):
    order = order_controller.get_order_by_number(order_number) 
    return dumps(order)

@order_bp.route('/api/order' , methods=['POST'])
def create_order():
    order = request.json
    order_id = order_controller.insert_order(order)
    return jsonify({'order_id': order_id})