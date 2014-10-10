# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 08:50:01 2014

@author: Gouthaman Balaraman
"""
import os
from flask import Flask, render_template, request, redirect
from flask.ext.security import login_required

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
TEMPLATE_FOLDER = os.path.join(BASEDIR,"templates")
STATIC_FOLDER   = os.path.join(BASEDIR,"static")

def create_app():
    app = Flask(__name__,
                template_folder = os.path.join(BASEDIR,"templates"),
                static_folder   = os.path.join(BASEDIR,"static"),
                static_url_path = "/static")
    
    app.config.from_object('app.config.DebugConfig')
    from app.forum.views import forum_bp
    app.register_blueprint(forum_bp)
    from flask.ext.sqlalchemy import SQLAlchemy
    db = SQLAlchemy(app)
    return app, db

app, db = create_app()

# Sample HTTP error handling
@app.errorhandler(404)
def not_found(error):
    return render_template('404.html'), 404

@app.before_request 
def remove_trailing_slash(): 
    if request.path != '/' and request.path.endswith('/'): 
        return redirect(request.path[:-1]) 

# default views
@app.route('/')
@login_required
def home():
    return render_template('index.html')