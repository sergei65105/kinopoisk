from django.urls import path

from kinopoisk.views import *

urlpatterns = [
    path('', main, name='main'),
    path('movies/', movie_list, name='movie_list'),
    path('actors/', actor_list, name='actor_list'),
    path('directors/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('person/<int:person_id>/', person_detail, name='person_detail'),
    path('genre/<int:genre_id>/', genre_detail, name='genre_detail'),
    path('add_movie_review/', add_movie_review, name='add_movie_review'),
    path('get_movie_reviews/', get_movie_reviews, name='get_movie_reviews'),
    path('get_genres/', get_genres, name='get_genres'),
    path('movie_review_vote/', movie_review_vote, name='movie_review_vote'),
]
