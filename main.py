from flask import Flask, render_template, url_for, request, flash, redirect
from forms import FormCriarConta, FormLogin
from flask_sqlalchemy import SQLAlchemy

''' 
    *   PROJETO DE CRIAÇÃO DE SITE COM O MICRO-FRAMWORK FLASK   *
'''

app = Flask(__name__)


app.config['SECRET_KEY'] = '08f071612996239d3f877c5601e24998'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///bancodados_mastertechnology.db'

db = SQLAlchemy(app)


@app.route("/")
def home():
    return render_template('home.html')


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
def usuarios():
    return render_template('usuarios.html')


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_logim' in request.form:
        flash(f'Login realizado com sucesso no e-mail {form_login.email.data}', 'alert-success')
        return redirect(url_for('home'))
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        flash(f'Conta criada com sucesso no e-mail {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


if __name__ == '__main__':
    app.run(
        debug=True)