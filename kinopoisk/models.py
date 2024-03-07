from django.db import models

from core.models import User


# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=300)
    rating = models.FloatField(null=True, blank=True)
    poster = models.ImageField(upload_to='kinopoisk/images/movie/poster/', null=True, blank=True)
    description = models.TextField()
    release_date = models.DateTimeField()
    duration = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField('Genre', related_name='movies')
    directors = models.ManyToManyField('MoviePerson', related_name='director_movies')
    actors = models.ManyToManyField('MoviePerson', related_name='actor_movies')
    budget = models.PositiveIntegerField()


class MoviePerson(models.Model):
    class RoleType(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        DIRECTOR = 'director', 'Director'

    name = models.CharField(max_length=200)
    birth_date = models.DateField()
    photo = models.ImageField(upload_to='kinopoisk/images/movie_person/photo/', null=True, blank=True)
    role = models.CharField(max_length=20, blank=True, null=True, choices=RoleType.choices)
    biography = models.TextField()


# director = MoviePerson.objects.get(id=1)
# director.movies.filter()
# director.movie_set.all()


class Genre(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(null=True, blank=True)


class MovieReview(models.Model):
    author = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE)
    text = models.TextField()
    likes = models.PositiveIntegerField(default=0)
    created_at = models.DateField(auto_now_add=True)

# доделать модели и мигрировать их
# отобразить в админке
