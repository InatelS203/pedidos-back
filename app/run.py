from flask import Flask
from config.db_config import init_db
from routes import stock_routes, order_routes
from flask_cors import CORS
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)
init_db()
CORS(app)

app.register_blueprint(stock_routes.stock_bp)
app.register_blueprint(order_routes.order_bp)

if __name__ == "__main__":
    app.run(debug=True)
