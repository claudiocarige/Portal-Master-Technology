from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField, ValidationError, TextAreaField
from mastertechnology.models import Usuarios
from flask_login import current_user

'''   FORMULÁRIOS   '''


class FormLogin(FlaskForm):
    email = StringField('E-mail', [validators.DataRequired(), validators.Email(message='** E-mail Inválido **')])
    senha = PasswordField('Senha', [validators.DataRequired(),
                                    validators.Length(min=6, max=20, message='** Senha Inválida **')])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_logim = SubmitField('Fazer Login')


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', [validators.DataRequired(), validators.Length(min=4, max=20)])
    email = StringField('E-mail', [validators.DataRequired(), validators.Email(message='** E-mail Inválido **')])
    senha = PasswordField('Senha', [validators.DataRequired(),
                                    validators.EqualTo('confirmacao_senha',
                                                       message='** As Senhas não correspondem **')])
    confirmacao_senha = PasswordField('Repita a Senha')
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuarios.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')


class FormCriarPost(FlaskForm):
    titulo = StringField('Título do Post', [validators.DataRequired(), validators.Length(min=4, max=140)])
    corpo_post = TextAreaField('Escreva seu texto aqui!', [validators.DataRequired()])
    botao_submit_criarpost = SubmitField('Criar Post')


class FormEditarPerfil(FlaskForm):
    username = StringField('Nome do Usuário', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('E-mail', [validators.DataRequired(), validators.Email(message='** E-mail Inválido **')])
    botao_submit_editarperfil = SubmitField('Atualizar')
    foto_perfil = FileField('Atualizar Foto de Perfil', validators=[FileAllowed(['jpg', 'png'])])
    linguagem_python = BooleanField('Python')
    linguagem_java = BooleanField('Java')
    linguagem_javascript = BooleanField('JavaScript')
    linguagem_php = BooleanField('PHP')
    linguagem_html = BooleanField('HTML')
    linguagem_css = BooleanField('CSS')
    linguagem_c = BooleanField('C')
    linguagem_c_mais_mais = BooleanField('C++')
    linguagem_c_sharp = BooleanField('C#')
    linguagem_ruby = BooleanField('Ruby')
    linguagem_euphoria = BooleanField('Euphoria')

    def validate_email(self, email):
        if current_user.email != email.data:
            usuario = Usuarios.query.filter_by(email=email.data).first()
            if usuario:
                raise ValidationError('Já existe um usuário com este E-mail. Cadastre outro e-mail para continuar.')


class FormCotacao(FlaskForm):
    moeda = StringField('Digite a Moeda.')
    botao_submit_cotacao = SubmitField('Cotar')


class FormBuscaCep(FlaskForm):
    cep = StringField('Digite o Cep.')
    botao_submit_cep = SubmitField('Buscar')