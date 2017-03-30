
from sqlalchemy.orm import sessionmaker, relationship

from app import db


class Cinema(db.Model):
    __tablename__ = 'cinema'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    genre_id = db.Column(db.Integer, db.ForeignKey('genre.id'),)
    director_id = db.Column(db.Integer, db.ForeignKey('director.id'))
    year_of_issue = db.Column(db.String(4))
    country_id = db.Column(db.Integer, db.ForeignKey('country.id'))
    is_viewed = db.Column(db.Boolean, nullable=False)


    def __init__(self, title, genre, year_of_issue, director, country):
        self.title = title
        self.genre_id = genre
        self.year_of_issue = year_of_issue
        self.director_id = director
        self.country_id = country
        self.is_viewed = False

    def __repr__(self):
        return "<Cinema('%s','%s', '%s', '%s', '%s')>" % (self.title, self.genre_id, self.director_id, self.country_id, self.is_viewed)


class Genre(db.Model):
    __tablename__ = 'genre'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    cinemas = db.relationship('Cinema', backref='genre', lazy='dynamic')

    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Genre('%s')>" % (self.title)

class Director(db.Model):
    __tablename__ = 'director'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    cinemas = db.relationship('Cinema', backref='director', lazy='dynamic')

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return "<Director('%s')>" % (self.name)

class Country(db.Model):
    __tablename__ = 'country'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(255), nullable=False)
    cinemas = db.relationship('Cinema', backref='country', lazy='dynamic')
    
    def __init__(self, title):
        self.title = title

    def __repr__(self):
        return "<Country('%s')>" % (self.title)

