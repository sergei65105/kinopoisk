from rest_framework import serializers

from kinopoisk.models import *


class GenreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = '__all__'


class MovieReviewSerializer(serializers.ModelSerializer):
    author_name = serializers.CharField(source='author.username', read_only=True)
    author = serializers.HiddenField(default=serializers.CurrentUserDefault())
    votes_count = serializers.SerializerMethodField()

    def get_votes_count(self, obj):
        return MovieReviewVote.objects.filter(review=obj).count()
    class Meta:
        model = MovieReview
        fields = '__all__'
