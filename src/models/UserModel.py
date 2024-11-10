from src.main import db

class User(db.model):
    id:int = db.Column(db.Integer, primary_key=True)
    user:str = db.Column(db.String(255), nullable=False)
    password:str = db.Column(db.String(255), nullable=False)
    data = db.Column(db.String(50), nullable=False)
    token:str = db.Column(db.String(255), nullable=False)