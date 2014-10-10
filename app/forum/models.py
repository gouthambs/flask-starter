# -*- coding: utf-8 -*-
"""
Created on Tue Oct 07 14:41:30 2014

@author: Gouthaman Balaraman
"""

from app import db
from datetime import datetime

question_followers = db.Table('question_followers',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('question_id', db.Integer(), db.ForeignKey('question.id'))
    )

    
question_topics = db.Table('question_topics',
        db.Column('topic_id', db.Integer(), db.ForeignKey('topic.id')),
        db.Column('question_id', db.Integer(), db.ForeignKey('question.id'))    
    )
    
    
topic_followers = db.Table('topic_followers',
        db.Column('user_id', db.Integer(), db.ForeignKey('user.id')),
        db.Column('topic_id', db.Integer(), db.ForeignKey('topic.id'))
    )
    

class Question(db.Model):
    id = db.Column(db.Integer(), primary_key=True)
    question = db.Column(db.String(127), unique=True)
    description = db.Column(db.String(255))
    topics = db.relationship("Topic", secondary=question_topics, 
                        backref=db.backref("questions_tagged", lazy='dynamic'))
    anonymous = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime())
    lastedit_at = db.Column(db.DateTime())
    # relationship to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', 
                         backref=db.backref('questions_asked',lazy='dynamic'))
    # relationship to votes
    votes = db.relationship('QuestionVotes',backref='question')
    # followers
    followers = db.relationship('User', secondary=question_followers,
                        backref=db.backref('questions_followed', lazy='dynamic'))
    def __init__ (self, question, description, topics, anonymous=False):
        self.question = question
        self.description = description
        self.topics = topics
        self.created_at = datetime.now()
        self.lastedit_at = datetime.now()
        self.anonymous = anonymous
        #self.tags = tags
    

class Answer(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    text = db.Column(db.Text)
    anonymous = db.Column(db.Boolean)
    created_at = db.Column(db.DateTime())
    lastedit_at = db.Column(db.DateTime())
    # relationship to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('answers', lazy='dynamic'))
    user_desc = db.Column(db.String(63))
    # relationship to question
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    question = db.relationship('Question', 
                               backref=db.backref('answers',lazy='dynamic'))
    # relationship to votes
    votes = db.relationship('AnswerVotes', backref='answer')

    
class QuestionVotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Boolean) #if false, its a downvote
    anonymous = db.Column(db.Boolean)
    # link to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('q_votes',lazy='dynamic')) 
    user_desc = db.Column(db.String(63))
    question_id = db.Column(db.Integer, db.ForeignKey('question.id'))
    
    
class AnswerVotes(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    upvote = db.Column(db.Boolean) #if false, its a downvote
    anonymous = db.Column(db.Boolean)
    # link to user
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    user = db.relationship('User', backref=db.backref('a_votes',lazy='dynamic'))    
    answer_id = db.Column(db.Integer, db.ForeignKey('answer.id'))
    
    
class Topic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(32), unique=True)
    description = db.Column(db.String(255))
    followers = db.relationship('User', secondary=topic_followers, 
                                backref = db.backref('topics',lazy='dynamic') )
    
    