from config.db_config import get_db

class StockModel:
    @staticmethod
    def get_stock():
        db = get_db()
        stock_collection = db['Menu']
        return stock_collection.find()