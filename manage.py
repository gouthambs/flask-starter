# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 08:40:50 2014

@author: Gouthaman Balaraman
"""

from flask import render_template
from flask.ext.security import login_required
from app import app, db
from app.auth.models import user_datastore
# Create app



# Create a user to test with
@app.before_first_request
def create_user():
    db.create_all()
    user_datastore.create_user(email='gouthambs@gmail.com', password='password')
    db.session.commit()

# Views
@app.route('/')
@login_required
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run()