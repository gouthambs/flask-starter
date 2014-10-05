# -*- coding: utf-8 -*-
"""
Created on Sat Mar 22 15:21:39 2014

@author: Goutham
"""
from flask import render_template,Blueprint,redirect,url_for,session,g
#from flask.ext.login import login_required,logout_user,current_user
from flask.ext.security import login_required, logout_user, current_user
from forms import LoginForm,RegisterForm
from app import TEMPLATE_FOLDER,STATIC_FOLDER,db
from models import User

auth_bp = Blueprint('auth',__name__,
                    template_folder = TEMPLATE_FOLDER,
                    static_folder = STATIC_FOLDER,
                    url_prefix = "/auth")


#@auth_bp.before_request
#def before_request():
#    g.user = current_user


