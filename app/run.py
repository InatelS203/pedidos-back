from flask import Flask
from config.db_config import init_db
from routes import stock_routes, order_routes

app = Flask(__name__)
init_db()

app.register_blueprint(stock_routes.stock_bp)
app.register_blueprint(order_routes.order_bp)

if __name__ == "__main__":
    app.run(debug=True)