from django.shortcuts import render

from kinopoisk.models import *


# Create your views here.
def main(request):
    return render(request, 'kinopoisk/main.html')


def movie_list(request):
    return render(request, 'kinopoisk/movie_list.html', {
        'movies': Movie.objects.all()
    })


def actor_list(request):
    return render(request, 'kinopoisk/person_list.html', {
        'persons': MoviePerson.objects.filter(role=MoviePerson.RoleType.ACTOR),
        'title': 'Актёры'
    })


def director_list(request):
    return render(request, 'kinopoisk/person_list.html', {
        'persons': MoviePerson.objects.filter(role=MoviePerson.RoleType.DIRECTOR),
        'title': 'Режиссёры'
    })


def genre_list(request):
    return render(request, 'kinopoisk/genre_list.html', {
        'genres': Genre.objects.all()
    })


def movie_detail(request, movie_id):
    return render(request, 'kinopoisk/detail/movie.html', {
        'movie': Movie.objects.get(id=movie_id)
    })


def actor_detail(request, actor_id):
    actor = MoviePerson.objects.get(id=actor_id)
    return render(request, 'kinopoisk/detail/person.html', {
        'person': actor,
        'movies': actor.acted_in_movies.all()
    })


def director_detail(request, director_id):
    director = MoviePerson.objects.get(id=director_id)
    return render(request, 'kinopoisk/detail/person.html', {
        'person': director,
        'movies': director.directed_movies.all()
    })


def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, 'kinopoisk/detail/genre.html', {
        'genre': genre,
        'movies': genre.movies.all()
    })
