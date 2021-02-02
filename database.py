from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__, template_folder='templates')
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgres+psycopg2://luisgc:Sk81398@localhost:5432/sinesis' # dialect+driver://username:password@host:port/database
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class User(db.Model):
    __tablename__ = 'user'
    name = db.Column(db.String(40))
    email = db.Column(db.String(120))
    password = db.Column(db.String(1000))
    init_date = db.Column(db.Date)
    id = db.Column(db.Integer, primary_key=True)
    
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password
        self.init_date = datetime.now().date()
        
    def AddUser(self, user):
        try:
            db.session.add(user)
            db.session.commit()
            
            return 'Usuario agregado correctamente.'
        except:
            db.session.rollback()
            return 'Error en los datos.'
    
    @staticmethod
    def AllUsers():
        return User.query.all()
    
    @staticmethod
    def User_by_id(user_id):
        return User.query.filter_by(id=user_id).first()