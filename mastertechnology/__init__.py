from flask import Flask
from flask_sqlalchemy import SQLAlchemy

''' 
    *   PROJETO DE CRIAÇÃO DE SITE COM O MICRO-FRAMWORK FLASK   *
'''

app = Flask(__name__)


app.config['SECRET_KEY'] = '08f071612996239d3f877c5601e24998'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodados_mastertechnology.db'

'''  CRIA O BANCO DE DADOS'''
db = SQLAlchemy(app)

'''   
        IMPORTAR O ARQUIVO LINK PARA PODER EXECUTAR AS PÁGINAS
        ELE PRECISA FICAR ABAIXO POIS O APP VAI SER CRIADO E DEPOIS 
        ELE VAI IMPORTAR OS LINKS
'''
from mastertechnology import links