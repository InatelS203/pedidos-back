from models.stock_model import StockModel

def get_stock_items():
    stock = StockModel.get_stock()
    return stock