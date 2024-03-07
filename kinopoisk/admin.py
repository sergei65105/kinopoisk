from django.contrib import admin

from kinopoisk.models import *


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_editable = (
        'poster',
        'rating',
    )
    list_display = (
        'title',
        'poster',
        'rating',
    )


@admin.register(MoviePerson)
class MoviePersonAdmin(admin.ModelAdmin):
    list_editable = (
        'photo',
        'role',
    )
    list_display = (
        'name',
        'photo',
        'role',
    )


@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):
    list_editable = (
        'description',
    )
    list_display = (
        'name',
        'description',
    )


@admin.register(MovieReview)
class MovieReviewAdmin(admin.ModelAdmin):
    list_editable = (
        'author',
        'movie',
        'text',
    )
    list_display = (
        'id',
        'author',
        'movie',
        'text',
    )
