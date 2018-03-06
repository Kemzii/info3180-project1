from flask_wtf import FlaskForm
from wtforms import Form, TextField, TextAreaField, validators, SelectField
from wtforms.validators import DataRequired, Email
from flask_wtf.file import FileField, FileRequired, FileAllowed

class MyForm(FlaskForm):
    firstname = TextField('First Name', validators=[DataRequired()])
    lastname = TextField('Last Name', validators=[DataRequired()])
    gender = SelectField('Gender', choices=[('Male'), ('Female')])
    email = TextField('Email', validators=[DataRequired(), Email()])
    location = TextField('Location', validators=[DataRequired()])
    biography = TextAreaField('Biography', validators=[DataRequired()])
    
    
class PhotoForm(FlaskForm):
    photo = FileField('Photo', validators=[
        FileRequired(),
        FileAllowed(['jpg', 'png', 'Images only!'])
    ])
    
    
