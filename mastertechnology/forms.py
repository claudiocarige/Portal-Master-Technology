from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, validators, BooleanField, ValidationError
from mastertechnology.models import Usuarios


'''   FORMULÁRIOS   '''


class FormLogin(FlaskForm):
    email = StringField('E-mail', [validators.DataRequired(), validators.Email(message='** E-mail Inválido **')])
    senha = PasswordField('Senha', [validators.DataRequired(),
                                    validators.Length(min=6, max=20, message='** Senha Inválida **')])
    lembrar_dados = BooleanField('Lembrar Dados de Acesso')
    botao_submit_logim = SubmitField('Fazer Login')


class FormCriarConta(FlaskForm):
    username = StringField('Nome do Usuário', [validators.DataRequired(), validators.Length(min=4, max=25)])
    email = StringField('E-mail', [validators.DataRequired(), validators.Email(message='** E-mail Inválido **')])
    senha = PasswordField('Senha', [validators.DataRequired(),
                                    validators.EqualTo('confirmacao_senha',message='** As Senhas não correspondem **')])
    confirmacao_senha = PasswordField('Repita a Senha')
    botao_submit_criarconta = SubmitField('Criar Conta')

    def validate_email(self, email):
        usuario = Usuarios.query.filter_by(email=email.data).first()
        if usuario:
            raise ValidationError('E-mail já cadastrado. Cadastre-se com outro e-mail ou faça login para continuar.')