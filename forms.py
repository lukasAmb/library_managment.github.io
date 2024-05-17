from flask_wtf import FlaskForm # type: ignore
from wtforms import StringField, PasswordField, SubmitField # type: ignore
from wtforms.validators import DataRequired, Length # type: ignore

class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=150)])
    password = PasswordField('Password', validators=[DataRequired(), Length(min=4, max=150)])
    submit = SubmitField('Login')

class BookForm(FlaskForm):
    title = StringField('Title', validators=[DataRequired()])
    author = StringField('Author', validators=[DataRequired()])
    borrower = StringField('Borrower')
    submit = SubmitField('Update')
