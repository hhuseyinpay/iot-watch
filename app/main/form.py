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


class NameDescriptionForm(FlaskForm):
    name = StringField('name', validators=[InputRequired(), Length(min=3, max=20)])
    description = StringField('description', validators=[InputRequired(), Length(min=0, max=200)])
    submit1 = SubmitField('Insert')


class IDNameDescriptionForm(FlaskForm):
    id = StringField('id', validators=[InputRequired(), Length(min=0, max=2000)])
    name = StringField('name', validators=[InputRequired(), Length(min=3, max=20)])
    description = StringField('description', validators=[InputRequired(), Length(min=0, max=200)])
    submit2 = SubmitField('Update')


class IDForm(FlaskForm):
    id = StringField('id', validators=[InputRequired(), Length(min=1, max=2000)])
    submit3 = SubmitField('Delete')
