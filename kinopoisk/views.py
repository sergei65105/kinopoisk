from django.views.decorators.csrf import csrf_exempt
from rest_framework import serializers
from django.http import JsonResponse
from django.shortcuts import render, redirect
import json

from rest_framework import status
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from kinopoisk.models import *
from kinopoisk.serializers import GenreSerializer, MovieReviewSerializer


# Create your views here.
def main(request):
    return render(request, 'kinopoisk/main.html')


def movie_list(request):
    return render(request, 'kinopoisk/movie_list.html', {
        'movies': Movie.objects.all().order_by('-id')
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


def person_detail(request, person_id):
    person = MoviePerson.objects.get(id=person_id)
    return render(request, 'kinopoisk/detail/person.html', {
        'person': person
    })


def genre_detail(request, genre_id):
    genre = Genre.objects.get(id=genre_id)
    return render(request, 'kinopoisk/detail/genre.html', {
        'genre': genre,
        'movies': genre.movies.all()
    })


@api_view(('POST',))
@permission_classes((IsAuthenticated,))
@csrf_exempt
def add_movie_review(request):
    serializer = MovieReviewSerializer(data=request.data, context={'request': request})
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(data=serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(('GET',))
def get_genres(request):
    genres = Genre.objects.all()
    return Response(GenreSerializer(genres, many=True).data, status=200)
    # return Response(GenreSerializer(genres[0]).data, status=200)


@api_view(('GET',))
def get_movie_reviews(request):
    movie_reviews = MovieReview.objects.filter(movie_id=request.GET['movieId'])
    return Response(
        MovieReviewSerializer(movie_reviews, many=True).data,
        status=status.HTTP_200_OK
    )


@api_view(('POST',))
@permission_classes((IsAuthenticated,))
def movie_review_vote(request):
    try:
        MovieReviewVote.objects.get(
            review_id=request.data['reviewId'],
            user_id=request.user.id
        ).delete()
        vote = False
    except MovieReviewVote.DoesNotExist:
        MovieReviewVote.objects.create(
            review_id=request.data['reviewId'],
            user_id=request.user.id
        )
        vote = True
    return Response({'vote': vote}, status=status.HTTP_200_OK)
