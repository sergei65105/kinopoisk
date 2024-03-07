from django.urls import path

from kinopoisk.views import main

urlpatterns = [
    path('', main, name='main'),
]

# movies
# actors
# directors
# geners

# movies/1/
# actors/1/
# directors/1/
# genres/1/
