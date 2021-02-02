from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Run


class AddRun(FlaskForm):
    km = DecimalField("KM")
