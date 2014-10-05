# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:33:43 2014

@author: Goutham
"""
from flask.ext.security import LoginForm, RegistrationForm



"""
from flask.ext.wtf import Form
from wtforms import TextField, PasswordField
from wtforms.validators import Required
from models import User

class LoginForm(Form):
    username = TextField('Username',validators= [Required()])
    password = PasswordField('Password' , validators=[Required()])
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        self.user = None
        
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False

        user = User.query.filter_by(
            username=self.username.data).first()
        if user is None:
            self.username.errors.append('Unknown username')
            return False

        if not user.valid_authentication(self.username.data,self.password.data):
            self.password.errors.append('Invalid password')
            return False

        self.user = user
        return True


class RegisterForm(Form):
    username = TextField('Username',validators= [Required()])
    password = PasswordField('Password' , validators=[Required()])
    email    = TextField('Email', validators=[Required()])
    
    def __init__(self, *args, **kwargs):
        Form.__init__(self, *args, **kwargs)
        
    def validate(self):
        rv = Form.validate(self)
        if not rv:
            return False
        user = User.query.filter_by(
            username=self.username.data).first()
        if user is not None:
            self.username.errors.append("Username already exists")
            return False
            
        user = User.query.filter_by(
            email=self.email.data).first()
        if user is not None:
            self.email.errors.append("Email already exists")
            return False
        return True
"""