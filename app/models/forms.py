from flask_wtf import FlaskForm
from datetime import date
from wtforms import StringField, PasswordField, IntegerField, BooleanField, DateField, FileField
from wtforms.validators import DataRequired

class VoteForm(FlaskForm):
    vote = IntegerField("Vote", validators = [DataRequired()])
