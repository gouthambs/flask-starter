# -*- coding: utf-8 -*-
"""
Created on Sun Oct 05 08:40:50 2014

@author: Gouthaman Balaraman
"""
from flask.ext.script import Manager
from app import app, db
from app.auth.models import user_datastore
# Create app


#manager = Manager()

# Create a user to test with
@app.before_first_request
def create_user():
    from app.auth.models import User
    from app.forum.models import Question, Answer, Topic
    db.create_all()
    user = User.query.filter(User.email=='gouthambs@gmail.com').all()
    if len(user)==0:
        user_datastore.create_user(email='gouthambs@gmail.com', password='password')
        db.session.commit()



if __name__ == '__main__':
    app.run()