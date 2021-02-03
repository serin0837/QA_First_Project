from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, PasswordField, BooleanField, SelectField, DecimalField, IntegerField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from application.models import Goal


class GoalForm(FlaskForm):
    goal_name = StringField("Goal Name", validators=[DataRequired()])
    goal_setdate = StringField("When you decide", validators=[DataRequired()])
    goal_finishdate = StringField(
        "When you want to finish", validators=[DataRequired()])
    goal_success = BooleanField("Success?")
    submit = SubmitField("Add Goal")
