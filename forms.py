from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, BooleanField, SelectField, TextAreaField
from wtforms.validators import InputRequired, Optional, URL, NumberRange

class AddPetForm(FlaskForm):

    name = StringField("Pet's Name", validators=[InputRequired(message="Must give pet a name")])

    species = SelectField("Species", choices=[("dog", "Dog"),("cat","Cat"),("porcupine","Porcupine")])

    photo_url = StringField("Photo URL", validators=[URL(require_tld=True, message="Please enter a valid URL"),Optional()])

    age = IntegerField("Pet's Age", validators=[NumberRange(min=0, max=30, message="Please enter age between 0 - 30"),Optional()])

    notes = TextAreaField("Pet Notes")

class EditPetForm(FlaskForm):
    
    photo_url = StringField("Photo URL", validators=[URL(require_tld=True, message="Please enter a valid URL"),Optional()])

    notes = TextAreaField("Pet Notes", validators=[Optional()])

    available = BooleanField("Available?")