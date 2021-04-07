from datetime import datetime
from app import db
from sqlalchemy import Column, String, Integer, Date
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class Area(db.Model): 
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))

    def __repr__(self):
        return f'<Area id: {self.id}, name: {self.name}>'

class Role(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))

    def __repr__(self):
        return f'<Role id: {self.id}, name: {self.name}>'

class User(db.Model, UserMixin):
    id = Column(Integer(), primary_key=True)
    user_name = Column(String(length=80))
    email = Column(String(length=100), unique=True)
    password_hash = Column(String(length=200))
    date = Column(Date(), default=datetime.now())
    area_id = Column(Integer(), db.ForeignKey('area.id'))
    role_id = Column(Integer(), db.ForeignKey('role.id'))
    
    @staticmethod
    def add(user):
        try:
            db.session.add(user)
            db.session.commit()
            return ('Usuario registrado con éxito')
        except:
            db.session.rollback()
            return ('Ha sucedido un problema, intente de nuevo más tarde')
        
    def set_password_hash(self, password):
        self.password_hash = generate_password_hash(password)
        db.session.commit()

    def __repr__(self):
        return f'<User id: {self.id}, user_name: {self.user_name}, area: {self.area_id}>'

class Theme(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    user_id = Column(Integer(), db.ForeignKey('user.id'))

    def __repr__(self):
        return f'<Theme id: {self.id}, name: {self.name}, owner: {self.user_id}>'

class Task(db.Model):
    id = Column(Integer(), primary_key=True)
    name = Column(String(length=80))
    date = Column(Date(), default=datetime.now())
    theme_id = Column(Integer(), db.ForeignKey('theme.id'))

    def __repr__(self):
        return f'<Task id: {self.id}, name: {self.name}, theme: {self.theme_id}>'