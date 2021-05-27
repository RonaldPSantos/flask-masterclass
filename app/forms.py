from flask_wtf import FlaskForm
from wtforms.fields.html5 import EmailField
from wtforms.fields import PasswordField, BooleanField, SubmitField, StringField, SelectField
from wtforms.validators import Length, Email, DataRequired
from app.models import Book


class LoginForm(FlaskForm):
    email = EmailField("Email", validators=[])
    password = PasswordField("Senha", validators=[
        Length(3, 9, "A senha deve conter entre 3 e 9 caracteres")
    ])
    remember = BooleanField("Permanecer Conectado")
    submit = SubmitField("Logar")


class RegisterForm(FlaskForm):
    name = StringField("Nome completo", validators=[
        DataRequired("Campo nome completo é obrigatório")
    ])
    email = EmailField("Email", validators=[])
    password = PasswordField("Senha", validators=[
        Length(3, 9, "A senha deve conter entre 3 e 9 caracteres")
    ])
    submit = SubmitField("Cadastrar")


class BookForm(FlaskForm):
    name = StringField("Nome do livro", validators=[
        DataRequired("Nome do livro é obrigatório")
    ])
    submit = SubmitField("Cadastrar")


class UserBookForm(FlaskForm):
    book = SelectField("Livro", coerce=int)
    submit = SubmitField("Cadastrar")

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.book.choices = [
            (book.id, book.name) for book in Book.query.all()
        ]
