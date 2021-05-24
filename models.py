# models.py

from app import db


class Clientes(db.Model):
    __tablename__ = 'Cliente'

    id_cliente = db.Column(db.Integer, primary_key=True)
    cpf = db.Column(db.String(11), nullable=False, index=True)
    telefone = db.Column(db.String(20))
    nome = db.Column(db.String(50), nullable=False)

    def __init__(self, cpf, telefone, nome):
        self.cpf = cpf
        self.telefone = telefone
        self.nome = nome

    def __repr__(self):
        return '<Cliente %r>' % self.nome
