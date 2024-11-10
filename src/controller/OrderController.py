from flask import request, jsonify
from service.OrderService import OrderService

class OrderController:
    @staticmethod
    def get_orders():
        return OrderService.get_orders()
    
    @staticmethod
    def update_order(order_id:int):
        return OrderService.update_order(order_id=order_id)
    
    @staticmethod
    def order_details(order_id:int):
        return OrderService.details_order(order_id=order_id)
    
    @staticmethod
    def delete_order(order_id:int):
        return OrderService.delete_order(order_id=order_id)
    @staticmethod
    def create_order():
        return OrderService.create_order()
    