from flask import Flask, request, render_template, flash
from flask_sqlalchemy import SQLAlchemy
import chardet, codecs
import csv
from sqlalchemy import func
import config

app = Flask(__name__)
app.config.from_object(config)

# http://flask-sqlalchemy.pocoo.org/2.1/quickstart/#a-minimal-application
db = SQLAlchemy(app)

if __name__ == '__main__':
<<<<<<< HEAD
    from models import *
    db.create_all()
    """ simple qwery to table with where
    
    print(db.session.query(Cinema).filter_by(year_of_issue='1935').all())
    for i in db.session.query(Cinema).filter_by(year_of_issue='1935').all():
        print(i.title, i.year_of_issue)"""
    
    dir = db.session.query(Director).filter_by(name='Стэнли Кубрик').all()
    for i in dir[0].cinemas.all():
        print(i.year_of_issue, i.title)
        
    print(db.session.query(Cinema.director_id, func.count(Cinema)).group_by(Cinema.director_id))
    
"""
Нужны запросы:
1. Полный список фильмов с подставленными странами, жанрами и режисерами
2. Список фильмов по режисеру, стране, году git и ПЕРИОДУ, множественный выбор
3. Конструкции вида count(*) group_by
4. 
"""
    
=======
    app.run()

>>>>>>> 08ac2bd3bdda1318522718fecfef7e5434ff4892

        
    

