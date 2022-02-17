import os.path
from tkinter import TRUE

basedir = os.path.abspath(os.path.dirname(__file__))

DEBUG = TRUE

SQLALCHEMY_DATABASE_URI = 'sqlite:///' + os.path.join(basedir, 'database.db')

