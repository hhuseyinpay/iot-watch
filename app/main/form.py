from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, TextField, TextAreaField, SubmitField, validators, ValidationError

from wtforms.validators import DataRequired, InputRequired, Email, Length, AnyOf


class SignUpForm(FlaskForm):
    ssn = StringField('ssn', validators=[DataRequired()])
    firstname = StringField('first_name', validators=[DataRequired()])
    lastname = StringField('last_name', validators=[DataRequired()])
    username = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])


class LoginForm(FlaskForm):
    # username = StringField('username', validators=[DataRequired()])
    # password = PasswordField('Password', validators=[DataRequired()])

    ssn = StringField('ssn', validators=[InputRequired(), Length(min=3, max=20)])
    password = PasswordField('password',
                             validators=[InputRequired(), Length(min=3, max=20)])
    submit = SubmitField("Login")
