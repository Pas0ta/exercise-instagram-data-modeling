import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine
from eralchemy2 import render_er

Base = declarative_base()

class Follower(Base):
    __tablename__ = 'follower'
    id = Column(Integer, primary_key=True)
    user_from_id = Column(String(250), nullable=False)
    user_to_id = Column(String(250), nullable=False)
    folluser = relationship('User', backref='follower', lazy=True)

class Comment(Base):
    __tablename__ = 'comment'
    id = Column(Integer, primary_key=True)
    comment_text = Column(String(250), nullable=False)
    author_id = Column(String(250), nullable=False)
    post_id = Column(String(250), nullable=False)
    commuser= relationship('User', backref='comment', lazy=True)
    commpost = relationship('Post', backref='comment', lazy=True)

class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    type = Column(String(250), nullable=False)
    url = Column(String(250), nullable=False)
    post_id = Column(String(250), nullable=False)
    mediapost = relationship('Post', backref='media', lazy=True)

class User(Base):
    __tablename__ = 'user'
    id = Column(Integer, primary_key=True)
    username = Column(String(250))
    firstname = Column(String(250))
    lastname = Column(String(250), nullable=False)
    email = Column(String(250), nullable=False)
    followid = Column(Integer, ForeignKey('follower.id'),
        nullable=False)
    postid = Column(Integer, ForeignKey('post.id'),
        nullable=False)
    commentid = Column(Integer, ForeignKey('comment.id'),
        nullable=False)

    def to_dict(self):
        return {}

class Post(Base):
    __tablename__ = 'post'
    id = Column(Integer, primary_key=True)
    user_id = Column(String(250))
    userid = Column(Integer, ForeignKey('user.id'),
        nullable=False)
    postmedia = Column(Integer, ForeignKey('media.id'),
        nullable=False)
    postcomment = Column(Integer, ForeignKey('comment.id'),
        nullable=False)
    
    

    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
