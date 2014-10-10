import os
basedir = os.path.abspath(os.path.dirname(__file__))

class DebugConfig(object):
    SITENAME = "Flask-Base"
    DEBUG = True
    SECRET_KEY = 'super-secret'
    #SQLALCHEMY_DATABASE_URI =  'sqlite:///..\\app.db'
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'app.db')