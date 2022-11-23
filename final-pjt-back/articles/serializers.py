from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content','created_at', 'updated_at', 'comment_set', )
        fields = ('id', 'title', 'content', 'user', 'username', 'created_at', 'updated_at', 'comment_set', 'like_users', 'hate_users', 'viewnums', 'movie_id',)
        read_only_fields = ('like_users', 'hate_users', 'user', 'viewnums',)

class CommentListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    
    class Meta:
        model = Comment
        # fields = ('id', 'article', 'title', 'created_at', 'updated_at')
        # read_only_fields = ('article', )
        fields = ('id', 'article', 'user', 'username', 'created_at', 'updated_at', 'content')
        read_only_fields = ('user', 'article', )

class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set', )
        fields = ('id', 'title', 'content', 'user', 'username', 'created_at', 'updated_at', 'comment_set', 'like_users', 'hate_users', 'viewnums', 'movie_id',)
        read_only_fields = ('like_users', 'hate_users', 'user', 'viewnums',)

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Comment
        # fields = ('id', 'article', 'title', 'content', 'created_at', 'updated_at', )
        # read_only_fields = ('article', )
        fields = ('id', 'article', 'user', 'username', 'content', 'created_at', 'updated_at', )
        read_only_fields = ('article', 'user', )

