from django.urls import path

from kinopoisk.views import *

urlpatterns = [
    path('', main, name='main'),
    path('movies/', movie_list, name='movie_list'),
    path('actors/', actor_list, name='actor_list'),
    path('directors/', director_list, name='director_list'),
    path('genres/', genre_list, name='genre_list'),
    path('movie/<int:movie_id>/', movie_detail, name='movie_detail'),
    path('actor/<int:actor_id>/', actor_detail, name='actor_detail'),
    path('director/<int:director_id>/', director_detail, name='director_detail'),
    path('genre/<int:genre_id>/', genre_detail, name='genre_detail'),
]
