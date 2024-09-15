from app import db


class Filme(db.Model):
    __tablename__ = 'filmes'
    id = db.Column(db.Integer, primary_key=True)
    nome = db.Column(db.String)
    genero = db.Column(db.String)
    ano = db.Column(db.Integer)
    sinopse = db.Column(db.String)
    diretor = db.Column(db.String)
    
    alugueis = db.relationship('Aluguel', back_populates='filme')

   