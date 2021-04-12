from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField, FileField

class LoginForm(FlaskForm):
    username = StringField('Username',validators=[])
    password = PasswordField('Password', validators=[])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')

#Not used yet
class PCForm(FlaskForm):
    reported_file = FileField('Reported Document',validators=[])
    suspected_files = FileField('Suspected Document', validators=[])
    submit = SubmitField('Upload')