from flask import render_template, redirect, url_for, flash, request, abort
from flask_login import current_user, login_user, logout_user, login_required
from mastertechnology import app, db, bcrypt
from mastertechnology.forms import FormLogin, FormCriarConta, FormEditarPerfil, FormCriarPost
from mastertechnology.models import Usuarios, Postagens
import secrets
import os
from PIL import Image
import requests
import json

'''   
    *   FUNÇÕES DE PÁGINA     
'''


@app.route("/", methods=['GET', 'POST'])
def home():
    cotacoes = requests.get('https://economia.awesomeapi.com.br/json/all')
    cotacoes_dicio = cotacoes.json()
    posts = Postagens.query.order_by(Postagens.id.desc())
    return render_template('home.html', posts=posts, cotacoes_dicio=cotacoes_dicio)


@app.route('/contato')
def contato():
    return render_template('contato.html')


@app.route('/usuarios')
@login_required
def usuarios():
    lista_usuarios = Usuarios.query.all()
    return render_template('usuarios.html', lista_usuarios=lista_usuarios)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form_login = FormLogin()
    form_criarconta = FormCriarConta()
    if form_login.validate_on_submit() and 'botao_submit_logim' in request.form:
        usuario = Usuarios.query.filter_by(email=form_login.email.data).first()
        if usuario and bcrypt.check_password_hash(usuario.senha, form_login.senha.data):
            login_user(usuario, remember=form_login.lembrar_dados.data)
            flash(f'Login realizado com sucesso no e-mail {form_login.email.data}', 'alert-success')
            page_next = request.args.get('next')
            if page_next:
                return redirect(page_next)
            else:
                return redirect(url_for('home'))
        else:
            flash(f'Falha no login. E-mail ou senha incorretos.', 'alert-danger')
    if form_criarconta.validate_on_submit() and 'botao_submit_criarconta' in request.form:
        senha_cript = bcrypt.generate_password_hash(form_criarconta.senha.data)
        usuario = Usuarios(username=form_criarconta.username.data, email=form_criarconta.email.data, senha=senha_cript)
        db.session.add(usuario)
        db.session.commit()
        flash(f'Conta criada com sucesso no e-mail {form_criarconta.email.data}', 'alert-success')
        return redirect(url_for('home'))
    return render_template('login.html', form_login=form_login, form_criarconta=form_criarconta)


@app.route('/perfil')
@login_required
def perfil():
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('perfil.html', foto_perfil=foto_perfil)


def salvar_imagem(imagem):
    codigo = secrets.token_hex(8)
    nome, extensao = os.path.splitext(imagem.filename)
    nome_completo = nome + codigo + extensao
    caminho_arquivo = os.path.join(app.root_path, 'static/fotos_perfil', nome_completo)
    tamanho = (200, 200)
    imagem_reduzida = Image.open(imagem)
    imagem_reduzida.thumbnail(tamanho)
    imagem_reduzida.save(caminho_arquivo)
    return nome_completo


def atualizar_linguagens(form):
    lista_linguagem = [campo.label.text for campo in form if 'linguagem_' in campo.name and campo.data]
    return ";".join(lista_linguagem)


@app.route('/perfil/editar', methods=['GET', 'POST'])
@login_required
def editar_perfil():
    form = FormEditarPerfil()
    if form.validate_on_submit():
        current_user.email = form.email.data
        current_user.username = form.username.data
        if form.foto_perfil.data:
            nome_imagem = salvar_imagem(form.foto_perfil.data)
            current_user.foto_perfil = nome_imagem
        current_user.linguagem = atualizar_linguagens(form)
        db.session.commit()
        flash('Edição efetuada com sucesso.', 'alert-success')
        return redirect(url_for('perfil'))
    elif request.method == "GET":
        form.email.data = current_user.email
        form.username.data = current_user.username
        if 'Python' in current_user.linguagem:
            form.linguagem_python.data = True
        elif 'Java' in current_user.linguagem:
            form.linguagem_java.data = True
        elif 'JavaScript' in current_user.linguagem:
            form.linguagem_javascript.data = True
        elif 'PHP' in current_user.linguagem:
            form.linguagem_php.data = True
        elif 'HTML' in current_user.linguagem:
            form.linguagem_html.data = True
        elif 'CSS' in current_user.linguagem:
            form.linguagem_css.data = True
        elif 'C' in current_user.linguagem:
            form.linguagem_c.data = True
        elif 'C++' in current_user.linguagem:
            form.linguagem_c_mais_mais.data = True
        elif 'C#' in current_user.linguagem:
            form.linguagem_c_sharp.data = True
        elif 'Ruby' in current_user.linguagem:
            form.linguagem_ruby = True
        elif 'Euphoria' in current_user.linguagem:
            form.linguagem_euphoria = True
    foto_perfil = url_for('static', filename='fotos_perfil/{}'.format(current_user.foto_perfil))
    return render_template('editarperfil.html', foto_perfil=foto_perfil, form=form)


@app.route('/post/criar', methods=['GET', 'POST'])
@login_required
def criar_post():
    form_post = FormCriarPost()
    if form_post.validate_on_submit():
        post = Postagens(titulo=form_post.titulo.data, corpo_post=form_post.corpo_post.data, autor=current_user)
        db.session.add(post)
        db.session.commit()
        flash('Post criado com Sucesso!', 'alert-success')
        return redirect(url_for('home'))
    return render_template('criarpost.html', form_post=form_post)


@app.route('/sair')
@login_required
def sair():
    logout_user()
    flash(f'Logout feito com sucesso.', 'alert-success')
    return redirect(url_for('home'))


@app.route('/post/<post_id>', methods=['GET', 'POST'])
@login_required
def exibir_post(post_id):
    post = Postagens.query.get(post_id)
    if current_user == post.autor:
        form_exibir_post = FormCriarPost()
        if request.method == 'GET':
            form_exibir_post.titulo.data = post.titulo
            form_exibir_post.corpo_post.data = post.corpo_post
        elif form_exibir_post.validate_on_submit():
            post.titulo = form_exibir_post.titulo.data
            post.corpo_post = form_exibir_post.corpo_post.data
            db.session.commit()
            flash('Post Atualizado com Sucesso.', 'alert-success')
            return redirect(url_for('home'))
    else:
        form_exibir_post = None
    return render_template('post.html', post=post, form_exibir_post=form_exibir_post)


@app.route('/post/<post_id>/excluir', methods=['GET', 'POST'])
@login_required
def excluir_post(post_id):
    excluirpost = Postagens.query.get(post_id)
    if current_user == excluirpost.autor:
        db.session.delete(excluirpost)
        db.session.commit()
        flash('Post excluido com sucesso.', 'alert-danger')
        return redirect(url_for('home'))
    else:
        abort(403)


