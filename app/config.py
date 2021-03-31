import os
class Config:
    SECRET_KEY=os.urandom(10)
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://luisg:Sk81398@localhost:5432/excer_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False