from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager


app = Flask(__name__)

app.config['SECRET_KEY'] = '08f071612996239d3f877c5601e24998'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodados_mastertechnology.db'

'''  
    *   BANCO DE DADOS
'''
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

'''
    *   LOGIN DE USUARIO
'''
login_usuario = LoginManager(app)
login_usuario.login_view = 'login'
login_usuario.login_message_category = 'alert-info'


from mastertechnology import links