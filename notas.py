import os
dbdir = os.path.abspath(os.path.dirname(__file__))
path = 'sqlite:///' + os.path.join(dbdir, 'excer.db')
print(path)
