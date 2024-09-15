from app import db

class Aluguel(db.Model):
    __tablename__ = 'alugueis'
    id = db.Column(db.Integer, primary_key=True)
    usuario_id = db.Column(db.Integer, db.ForeignKey('usuarios.id'))
    filme_id = db.Column(db.Integer, db.ForeignKey('filmes.id'))
    data_aluguel = db.Column(db.DateTime)
    nota = db.Column(db.Integer)
    usuario = db.relationship('Usuario')
    filme = db.relationship('Filme')