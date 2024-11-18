from models.order_model import OrderModel
from commands.command import Command

class CreateOrderCommand(Command):
    def __init__(self, order_data):
        self.order_data = order_data

    def execute(self):
        return OrderModel.insert_order(self.order_data)

class GetOrderCommand(Command):
    def __init__(self):
        pass

    def execute(self):
        return OrderModel.get_order()

class GetOrderByNumberCommand(Command):
    def __init__(self, order_number):
        self.order_number = order_number

    def execute(self):
        return OrderModel.get_order_by_number(self.order_number)