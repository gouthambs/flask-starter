# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 08:50:01 2014

@author: Gouthaman Balaraman
"""
import os
from flask import Flask, render_template
from flask.ext.security import login_required

BASEDIR = os.path.abspath(os.path.join(os.path.dirname(__file__),'..'))
TEMPLATE_FOLDER = os.path.join(BASEDIR,"templates")
STATIC_FOLDER   = os.path.join(BASEDIR,"static")


app = Flask(__name__,
            template_folder = os.path.join(BASEDIR,"templates"),
            static_folder   = os.path.join(BASEDIR,"static"),
            static_url_path = "/static")

app.config.from_object('app.config.DebugConfig')



from flask.ext.sqlalchemy import SQLAlchemy
db = SQLAlchemy(app)


# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')