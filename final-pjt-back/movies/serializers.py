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
        fields = ('id', 'movie', 'user', 'content', 'rank', 'created_at', 'like_movie_comment_users', 'hate_movie_comment_users')
        read_only_fields = ('movie', 'user', 'like_movie_comment_users', 'hate_movie_comment_users',)


