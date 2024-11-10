from flask import Blueprint
from controller.OrderController import OrderController

orders_routes = Blueprint('orders', __name__)

@orders_routes.route('/orders', methods=['GET'])
def get_orders():
    return OrderController.get_orders()

@orders_routes.route('/orders/details/<int:order_id>',methods=['GET'])
def order_details(order_id:int):
    return OrderController.order_details(order_id=order_id)

@orders_routes.route('/orders/delete/<int:order_id>', methods=['DELETE'])
def order_delete(order_id:int):
    return OrderController.delete_order(order_id=order_id)

@orders_routes.route('/orders/update/<int:order_id>', methods=['PUT'])
def order_update(order_id:int):
    return OrderController.update_order(order_id=order_id)

@orders_routes.route('/create_order',methods=['POST'])
def create_order():
    return OrderController.create_order()
           
