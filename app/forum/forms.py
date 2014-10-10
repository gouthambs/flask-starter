# -*- coding: utf-8 -*-
"""
Created on Fri Oct 10 03:58:21 2014

@author: Gouthaman Balaraman
"""

from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.widgets import TextArea
from wtforms.validators import DataRequired

class QuestionForm(Form):
    question = StringField('Question', validators=[DataRequired()])
    description = StringField('Description', widget=TextArea())
    tags = StringField("Tags", validators=[DataRequired()])