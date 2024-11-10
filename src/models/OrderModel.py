from src.main import db
from datetime import datetime

class Order(db.Model) :
    id: int = db.Column(db.Integer, primary_key=True)  # ID do pedido (chave primária)
    description: str = db.Column(db.String(255), nullable=False)  # Descrição do pedido
    value: float = db.Column(db.Float, nullable=False)  # Valor do pedido
    data: str = db.Column(db.String(50), nullable=False)  # Data do pedido (como string)
    status: str = db.Column(db.String(50), nullable=False)  # Status do pedido

    status_list = ['Preparando', 'Em rota', 'Entregue' ]

    def to_dict(self) -> dict:
        return {
            'id': self.id,
            'description': self.description,
            'value': self.value,
            'status': self.status
        }
    
    def set_status(self, status:str):
        if status not in self.status_list:
            raise 'Status invalido'
        self.status = status
