from flask import Flask
from config.db_config import init_db
from routes.stock_routes import stock_bp

app = Flask(__name__)
init_db()

app.register_blueprint(stock_bp)

if __name__ == "__main__":
    app.run(debug=True)