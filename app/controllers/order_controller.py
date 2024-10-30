from models.order_model import OrderModel

def get_order_items():
    order = OrderModel.get_order()
    return order

def get_order_by_number(order_number):
    order = OrderModel.get_order_by_number(order_number)
    return order

def insert_order(order):
    order = OrderModel.insert_order(order)
    return order