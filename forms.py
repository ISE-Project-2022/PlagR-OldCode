from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[])
    password = PasswordField('Password', validators=[])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')