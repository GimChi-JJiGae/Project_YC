from rest_framework import serializers
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

    password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User

        # fields = ('id', 'username', 'password', 'age', 'sex', 'email', )
        fields = ('id', 'username', 'like_movies', 'movie_comments',
                  'password', 'age', 'sex', 'email', 'followings', 
                  'like_movie_comments', 'hate_movie_comments', 'followers',
                  'like_articles', )
                  
        read_only_fields = ('followings', 'like_movie_comments', 'movie_comments',
                            'hate_movie_comments', 'like_movies', 'followers',
                            'like_articles', )