# -*- coding: utf-8 -*-
"""
Created on Wed Oct 08 12:39:12 2014

@author: Gouthaman Balaraman
"""

from flask import Blueprint, request, render_template
from flask.ext.security.core import current_user
from flask.ext.security import login_required
from app import TEMPLATE_FOLDER, STATIC_FOLDER
from forms import QuestionForm



forum_bp = Blueprint('forum',__name__,
                    template_folder = TEMPLATE_FOLDER,
                    static_folder = STATIC_FOLDER,
                    url_prefix = "/forum")
                    



@forum_bp.route('/addq', methods=["GET", "POST"])
@login_required
def add_question():
    form = QuestionForm()
    if request.method == 'GET':
        
        return render_template("forum/add_question.html", form=form)
    else:
        try:
            from app import db
            from models import Question, Topic
            #if current_user.is_authenticated():
            topic_list = [request.form['tags']]
            topics = [ ]
            for topic_name in topic_list:
                t = Topic.query.filter_by(name=topic_name).all()
                print t
                if t != []:
                    topics.append(t[0])
            
            question = Question(request.form['question'], request.form['description'], 
                                topics)
            print request.form
            db.session.add(question)
            db.session.commit()
                
        except Exception as e:
            print str(e)
        finally:
            return
            return render_template("index.html")