from config.order_DAO import OrderDAO

class OrderModel:
    COLLECTION_NAME = 'PEDIDOS'

    @staticmethod
    def get_order():
        return OrderDAO.find(OrderModel.COLLECTION_NAME)

    @staticmethod
    def get_order_by_number(order_number):
        query = {"order_info.order_number": int(order_number)}
        order = OrderDAO.find_one(OrderModel.COLLECTION_NAME, query)
        
        if order:
            OrderDAO.update_one(OrderModel.COLLECTION_NAME, {"_id": order["_id"]}, {"$set": {"order_info.status": "done"}})
            
            next_query = {"order_info.order_number": int(order_number) + 1}
            next_order = OrderDAO.find_one(OrderModel.COLLECTION_NAME, next_query)
            if next_order:
                OrderDAO.update_one(OrderModel.COLLECTION_NAME, {"_id": next_order["_id"]}, {"$set": {"order_info.status": "doing"}})
        
        return OrderDAO.find_one(OrderModel.COLLECTION_NAME, query)

    @staticmethod
    def get_last_order_number():
        last_order = OrderDAO.find_one(OrderModel.COLLECTION_NAME, {}, sort=[("order_info.order_number", -1)])
        if last_order:
            return last_order["order_info"]["order_number"]
        return 0

    @staticmethod
    def insert_order(order):
        order_number = OrderModel.get_last_order_number() + 1
        order_status = 'doing' if order_number == 1 else 'to do'
        
        order_data = order[0]
        total_cost = sum(item['total_price'] for item in order_data['cart'])
        
        order_formatted = {
            'order_info': {
                'order_number': order_number,
                'status': order_status,
                'total_cost': total_cost,
            },
            'cart': order_data['cart']
        }
        
        return str(OrderDAO.insert_one(OrderModel.COLLECTION_NAME, order_formatted))
