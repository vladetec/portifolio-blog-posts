from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, ValidationError, TextAreaField
from wtforms.validators import DataRequired, EqualTo, Length
from wtforms.widgets import TextArea
from flask_ckeditor import CKEditorField
from flask_wtf.file import FileField

# Create A Search Form


class SearchForm(FlaskForm):
    searched = StringField("Perquisar", validators=[DataRequired()])
    submit = SubmitField("Enviar")


# Create Login Form
class LoginForm(FlaskForm):
    username = StringField("Username", validators=[DataRequired()])
    password = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Enviar")


# Create a Posts Form
class PostForm(FlaskForm):
    title = StringField("Titulo", validators=[DataRequired()])
    #content = StringField("Content", validators=[DataRequired()], widget=TextArea())
    content = CKEditorField('Conteudo', validators=[DataRequired()])

    #author = StringField("Author")
    slug = StringField("Slug", validators=[DataRequired()])
    submit = SubmitField("Enviar")

# Create a Form Class


class UserForm(FlaskForm):
    name = StringField("Nome", validators=[DataRequired()])
    username = StringField("Username", validators=[DataRequired()])
    email = StringField("Email", validators=[DataRequired()])
    favorite_color = StringField("Cor Favorita")
    about_author = TextAreaField("Sobre Autor")
    password_hash = PasswordField('Password', validators=[DataRequired(), EqualTo(
        'password_hash2', message='Passwords Must Match!')])
    password_hash2 = PasswordField(
        'Confirma Password', validators=[DataRequired()])
    profile_pic = FileField("Figura")
    submit = SubmitField("Enviar")


class PasswordForm(FlaskForm):
    email = StringField("Seu Email", validators=[DataRequired()])
    password_hash = PasswordField("Sua Senha", validators=[DataRequired()])
    submit = SubmitField("Enviar")

# Create a Form Class


class NamerForm(FlaskForm):
    name = StringField("Seu nome", validators=[DataRequired()])
    submit = SubmitField("Enviar")

    # BooleanField
    # DateField
    # DateTimeField
    # DecimalField
    # FileField
    # HiddenField
    # MultipleField
    # FieldList
    # FloatField
    # FormField
    # IntegerField
    # PasswordField
    # RadioField
    # SelectField
    # SelectMultipleField
    # SubmitField
    # StringField
    # TextAreaField

    # Validators
    # DataRequired
    # Email
    # EqualTo
    # InputRequired
    # IPAddress
    # Length
    # MacAddress
    # NumberRange
    # Optional
    # Regexp
    # URL
    # UUID
    # AnyOf
    # NoneOf
