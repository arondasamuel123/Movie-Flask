from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms import StringField, PasswordField, BooleanField, SubmitField
from wtforms.validators import Required,Email,EqualTo
from wtforms import ValidationError
from ..models import User

class RegistrationForm(FlaskForm):
    email= StringField('Your Email Address', validators=[Required(),Email()])
    username= StringField('Your Username', validators=[Required()])
    pass_secure= PasswordField('Password', validators=[Required(),EqualTo('password_confirm',message='Password must match')])
    
    password_confirm = PasswordField('Confirm Password',validators=[Required()])
    submit = SubmitField('Sign Up')
    
    
    def validate_email(self, data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('Email already exists')
    
    def validate_username(self, data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('Username already exists')
    

class LoginForm(FlaskForm):
    email = StringField('Your Email Address', validators=[Required(), Email()])
    password = PasswordField('Enter Password', validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Login')
     
    
    