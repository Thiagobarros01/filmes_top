from app import db

class Usuario(db.Model):
    __tablename__ = 'usuarios'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    celular = db.Column(db.Integer)
    email = db.Column(db.String, unique = True)
    aluguel = db.relationship('Aluguel')
    