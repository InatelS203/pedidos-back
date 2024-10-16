from config.db_config import get_db

class OrderModel:
    @staticmethod
    def get_order():
        db = get_db()
        order_collection = db['PEDIDOS']
        return order_collection.find()
    
    @staticmethod
    def get_order_by_number(order_number):
        db = get_db()
        order_collection = db['PEDIDOS']
        order = order_collection.find_one({"order_info.order_number": int(order_number)})
        order_collection.update_one({"_id": order["_id"]}, {"$set": {"order_info.status": "done"}})
        result = order_collection.find_one(sort=[("order_info.order_number", int(order_number))])

        
        next_order = order_collection.find_one({"order_info.order_number": result["order_info"]["order_number"] + 1})
        if next_order:
            order_collection.update_one({"_id": next_order["_id"]}, {"$set": {"order_info.status": "doing"}})
        return result
    
    @staticmethod
    def get_last_order_number():
        db = get_db()
        order_collection = db['PEDIDOS']
        last_order = order_collection.find_one(sort=[("order_info.order_number", -1)])
        if last_order:
            return last_order["order_info"]["order_number"]
        return 0

    @staticmethod
    def insert_order(order):
        db = get_db()
        order_collection = db['PEDIDOS']
        
        order_number = OrderModel.get_last_order_number() + 1
        if order_number == 1:
            order_status = 'doing'
        else:
            order_status = 'to do'
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
        
        return str(order_collection.insert_one(order_formatted).inserted_id)

