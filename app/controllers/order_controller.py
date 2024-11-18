from commands.invoker import CommandInvoker
from commands.order_commands import CreateOrderCommand, GetOrderCommand, GetOrderByNumberCommand

def get_order_items():
    command = GetOrderCommand()
    return CommandInvoker().execute(command)

def get_order_by_number(order_number):
    command = GetOrderByNumberCommand(order_number)
    return CommandInvoker().execute(command)

def insert_order(order):
    command = CreateOrderCommand(order)
    return CommandInvoker().execute(command)
