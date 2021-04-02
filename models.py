from datetime import datetime
from app import db
from sqlalchemy import Column, String, Integer, Date

class Area(db.Model): 
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))

    def __repr__():
        return f'<Area id: {id}, name: {name}>'

class Role(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))

    def __repr__():
        return f'<Role id: {id}, name: {name}>'

class User(db.Model):
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(length=80))
    email = Column(String(length=100), unique=True)
    password_hash = Column(String(length=200))
    date = Column(Date(), default=datetime.now())
    area_id = Column(Integer(), db.ForeignKey('area.id'))
    role_id = Column(Integer(), db.ForeignKey('role.id'))

    def __repr__():
        return f'<Group id: {id}, name: {name}, area: {area_id}>'

class Theme(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    user_id = Column(Integer(), db.ForeignKey('user.id'))

    def __repr__():
        return f'<Group id: {id}, name: {name}, owner: {user_id}>'

class Task(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    date = Column(Date(), default=datetime.now())
    theme_id = Column(Integer(), db.ForeignKey('theme.id'))

    def __repr__():
        return f'<Task id: {id}, name: {name}, theme: {theme_id}>'