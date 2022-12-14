from mastertechnology import db, login_usuario
from datetime import datetime
from flask_login import UserMixin

'''  
     *   Classes dos Formulários  
'''


@login_usuario.user_loader
def load_usuario(id_usuario):
    return Usuarios.query.get(int(id_usuario))


class Usuarios(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String, unique=True, nullable=False)
    email = db.Column(db.String, unique=True, nullable=False)
    senha = db.Column(db.String, nullable=False)
    foto_perfil = db.Column(db.String, default='default.jpg')
    postagens = db.relationship('Postagens', backref='autor', lazy=True)
    linguagem = db.Column(db.String, nullable=False, default="Não informado")

    def contagem_post(self):
        return len(self.postagens)


class Postagens(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    titulo = db.Column(db.String, nullable=False)
    corpo_post = db.Column(db.Text, nullable=False)
    data_criacao = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)
    id_usuario = db.Column(db.Integer, db.ForeignKey('usuarios.id'), nullable=False)
