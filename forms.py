from flask_wtf import FlaskForm
from wtforms import TextAreaField, validators, RadioField, SubmitField, FileField
from wtforms.validators import DataRequired, InputRequired

class cForm(FlaskForm):
  text = TextAreaField(validators=[DataRequired()])
  choices = RadioField(validators=[DataRequired(), InputRequired()], choices = [
    ('b64d', 'From Base64'),
    ('b64e', 'To Base64'),
    ('hexd', 'From Hex'),
    ('hexe', 'To Hex'),
    ('r13d', 'From ROT13'),
    ('r13e', 'To ROT13'),
    ('urld', 'URL Decode'),
    ('urle', 'URL Encode'),
    ])
  submit = SubmitField("Upload File")

class sForm(FlaskForm):
  file = FileField("File upload")
  submit = SubmitField("Rip The File...")