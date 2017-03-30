from flask_wtf import FlaskForm
from wtforms import fields, validators
from wtforms_alchemy import ModelForm

from models import Cinema, Genre, Director


class CinemaForm(ModelForm):
    class Meta:
        model = Cinema
        include = [
            'genre_id',
            'director_id',
        ]

class GenreForm(ModelForm):
    class Meta:
        model = Genre


class DirectorForm(ModelForm):
    class Meta:
        model = Director
