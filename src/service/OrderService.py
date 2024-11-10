


class OrderService:

    @staticmethod
    def get_orders():
        return 'todos os pedidos'
    
    @staticmethod
    def get_order_by_id(order_id: int):
        return 'dado especiffico'
    
    @staticmethod
    def delete_order(order_id:int):
        return 'delete order'
    
    @staticmethod
    def details_order(order_id:int):
        return 'detalhes'
    
    @staticmethod 
    def update_order(order_id:int):
        return 'dado atualizado'
    
    @staticmethod
    def create_order():
        return 'criar o pedido'