from flask import Flask
from routes.OrderRoutes import orders_routes
from routes.TokenRoutes import token_routes
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

app = Flask(__name__)

db.init_app(app)

app.register_blueprint(orders_routes)
app.register_blueprint(token_routes)


if __name__ == "__main__":
    app.run(debug=True)