from config.db_config import get_db

class OrderDAO:
    @staticmethod
    def get_collection(collection_name):
        db = get_db()
        return db[collection_name]

    @staticmethod
    def find(collection_name, query=None):
        collection = OrderDAO.get_collection(collection_name)
        return collection.find(query or {})

    @staticmethod
    def find_one(collection_name, query, sort=None):
        collection = OrderDAO.get_collection(collection_name)
        if sort:
            return collection.find_one(query, sort=sort)
        return collection.find_one(query)

    @staticmethod
    def insert_one(collection_name, data):
        collection = OrderDAO.get_collection(collection_name)
        return collection.insert_one(data).inserted_id

    @staticmethod
    def update_one(collection_name, query, update_data):
        collection = OrderDAO.get_collection(collection_name)
        return collection.update_one(query, update_data)
