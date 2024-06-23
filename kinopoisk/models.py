from django.db import models

from Core.models import User


class MoviePerson(models.Model):
    class RoleType(models.TextChoices):
        ACTOR = 'actor', 'Actor'
        DIRECTOR = 'director', 'Director'

    name = models.CharField(max_length=255)
    birth_date = models.DateField(blank=True, null=True)
    photo = models.ImageField(
        upload_to="kinopoisk/images/person/photos/",
        blank=True, null=True)
    role = models.CharField(
        max_length=20, choices=RoleType.choices,
        blank=True, null=True)

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField(max_length=255, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class SibnetPlayer(models.Model):
    id = models.BigIntegerField(primary_key=True)


class Movie(models.Model):
    title = models.CharField(max_length=355)
    description = models.TextField()
    release_date = models.DateField(null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    # Продолжительность в минутах
    duration = models.PositiveSmallIntegerField()
    genres = models.ManyToManyField(Genre, related_name='movies')
    directors = models.ManyToManyField(
        MoviePerson, related_name='directed_movies'
    )
    budget = models.PositiveIntegerField()
    actors = models.ManyToManyField(
        MoviePerson, related_name='acted_in_movies')
    poster = models.ImageField(
        upload_to="kinopoisk/images/movies/posters/",
        blank=True, null=True)
    player = models.OneToOneField(to=SibnetPlayer, on_delete=models.SET_NULL, null=True)


class MovieReview(models.Model):
    author = models.ForeignKey(
        User, on_delete=models.SET_NULL,
        null=True, related_name='reviews')
    movie = models.ForeignKey(
        Movie, on_delete=models.CASCADE,
        related_name='reviews')
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


class MovieReviewVote(models.Model):
    review = models.ForeignKey(MovieReview,
                               on_delete=models.CASCADE,
                               related_name='votes')
    user = models.ForeignKey(User, on_delete=models.CASCADE,
                             related_name='votes')

    class Meta:
        unique_together = ('review', 'user')
