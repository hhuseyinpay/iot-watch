from flask_wtf import FlaskForm
from wtforms import StringField
from wtforms.validators import DataRequired, Length, Email


class SignUp(FlaskForm):
    ssn = StringField('ssn', validators=[DataRequired()])
    first_name = StringField('first_name', validators=[DataRequired()])
    last_name = StringField('last_name', validators=[DataRequired()])
    user_name = StringField('username', validators=[DataRequired()])
    password = StringField('password', validators=[DataRequired()])
    description = StringField('description', validators=[DataRequired()])
