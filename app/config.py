import os
dbdir = os.path.abspath(os.path.dirname(__file__))
from pathlib import Path
path = Path(dbdir)
dbdir = path.parent
class Config:
    SECRET_KEY=os.urandom(10)
    SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(dbdir, 'excer.db') #or 'postgresql+psycopg2://luisg:Sk81398@localhost:5432/excer_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False