from flask_wtf import FlaskForm
from wtforms import StringField,FloatField,SelectField,IntegerField,BooleanField
from wtforms.validators import input_required,NumberRange,EqualTo,URL,Optional

class addPetForm(FlaskForm):
    name = StringField('Name of pet',validators=[input_required()])
    species = SelectField('Species of pet',choices=[('cat','Cat'),('dog','Dog'),('porcupine','Porcupine')],validators=[input_required()])
    photo_url = StringField('Photo URL of pet',validators=[Optional(), URL(message='Invalid URL')])
    age = IntegerField('Age of pet', validators=[NumberRange(min=0, max=30)])
    notes = StringField('Notes about the pet')
    available = BooleanField('Availablity of pet',validators=[input_required()])
