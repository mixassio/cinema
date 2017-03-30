from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import chardet, codecs
import csv

import config

app = Flask(__name__)
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)

if __name__ == '__main__':
    from models import *
    db.create_all()
    
    print(db.session.query(Cinema).filter_by(year_of_issue='1960'))

        
    

