from flask_wtf import FlaskForm
from wtforms import SubmitField

class MultiChoice(FlaskForm):
    submit = SubmitField('Submit')
