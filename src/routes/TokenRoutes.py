from flask import Blueprint
from controller.TokenController import TokenControlerr

token_routes = Blueprint('users', __name__)

@token_routes.route('/token',methods=['POST'])
def create_token(user:str, password:str):
    return TokenControlerr.create_token(user=user,password=password)
