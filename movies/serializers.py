from rest_framework import serializers
from .models import Movie


class MovieSerializer(serializers.ModelSerializer):

    class Meta:
        model = Movie
        fields = ('name', 'imdb_score', 'popularity', 'director')
