from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bcrypt import Bcrypt
from flask_login import LoginManager

''' 
    *   PROJETO DE CRIAÇÃO DE SITE COM O MICRO-FRAMWORK FLASK   *
'''

app = Flask(__name__)


app.config['SECRET_KEY'] = '08f071612996239d3f877c5601e24998'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodados_mastertechnology.db'

'''  CRIA O BANCO DE DADOS'''
db = SQLAlchemy(app)

bcrypt = Bcrypt(app)

'''GERENCIADOR DE LOGIN DE USUARIO'''
login_usuario = LoginManager(app)
login_usuario.login_view = 'login'
login_usuario.login_message_category = 'alert-info'


'''   
        IMPORTAR O ARQUIVO LINK PARA PODER EXECUTAR AS PÁGINAS
        ELE PRECISA FICAR ABAIXO POIS O APP VAI SER CRIADO E DEPOIS 
        ELE VAI IMPORTAR OS LINKS
'''
from mastertechnology import links