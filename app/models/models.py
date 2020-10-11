from flask import request
from datetime import datetime
from . import db


class Course(db.Document):
    # id = db.Column(db.Integer, primary_key=True)
    title = db.StringField(max_length=80, required=True, unique=True)
    url = db.URLField(max_length=200, required=True, unique=True)
    created_at = db.DateTimeField(default=datetime.now)
    # reviews = db.relationship('Review', backref='course', lazy=True)
    meta = {'collection': 'course'}

    def __repr__(self):
        return f'{self.__class.__name__}({self.title},{self.url})'


class Review(db.Document):
    # id = db.Column(db.Integer, primary_key=True)
    course = db.LazyReferenceField('Course', dbref=True)
    rating = db.IntField()
    comment = db.StringField()
    created_at = db.DateTimeField(default=datetime.now)

    def __repr__(self):
        return f'{self.__class__.__name__}({self.created_at},{self.comment[:30]})'
