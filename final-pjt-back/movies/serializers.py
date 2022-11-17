from rest_framework import serializers
from .models import Movie, Genre, MovieComment

class MovieSerializer(serializers.ModelSerializer):

    class Meta:

        model = Movie
        fields = '__all__'
        read_only_fields = ('like_users',)

class MovieCommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = MovieComment
        fields = '__all__'
        read_only_fields = ('user', 'movie', 'like_movie_comment_users', 'hate_movie_comment_users', )