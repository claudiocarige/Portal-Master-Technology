from main import db
from datetime import datetime


class Usurious(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)
    foto_perfil = db.Column(db.String, default='default.jpg')
    postagens = db.relationship('Postagens', backref='autor', lazy=True)


class Postagens(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    corpo_post = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usurious.id'), nullable=False)

