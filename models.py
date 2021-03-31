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

class Group(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    area_id = Column(Integer(), db.ForeignKey('area.id'))

    def __repr__():
        return f'<Group id: {id}, name: {name}, area: {area_id}>'

class User(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    date = Column(Date())
    area_id = Column(Integer(), db.ForeignKey('area.id'))
    group_id = Column(Integer(), db.ForeignKey('group.id'))
    role_id = Column(Integer(), db.ForeignKey('role.id'))

    def __repr__():
        return f'<Group id: {id}, name: {name}, area: {area_id}>'

class Task(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    date = Column(Date())
    group_id = Column(Integer(), db.ForeignKey('group.id'))

    def __repr__():
        return f'<Task id: {id}, name: {name}, group: {group_id}>'