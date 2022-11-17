from rest_framework import serializers
from .models import Article, Comment

class ArticleListSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content','created_at', 'updated_at', 'comment_set', )
        fields = ('id', 'title', 'content', 'user', 'username', 'created_at', 'updated_at', 'comment_set', )
        read_only_fields = ('like_users', 'user', )

class CommentListSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = Comment
        # fields = ('id', 'article', 'title', 'created_at', 'updated_at')
        # read_only_fields = ('article', )
        fields = ('id', 'article', 'user', 'title', 'created_at', 'updated_at')
        read_only_fields = ('user', 'article', )

class ArticleSerializer(serializers.ModelSerializer):
    username = serializers.CharField(source='user.username', read_only=True)
    comment_set = CommentListSerializer(many=True, read_only=True)

    class Meta:
        model = Article
        # fields = ('id', 'title', 'content', 'created_at', 'updated_at', 'comment_set', )
        fields = ('id', 'title', 'content', 'user', 'username', 'created_at', 'updated_at', 'comment_set', )
        read_only_fields = ('like_users', 'user', )

class CommentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        # fields = ('id', 'article', 'title', 'content', 'created_at', 'updated_at', )
        # read_only_fields = ('article', )
        fields = ('id', 'article', 'user', 'title', 'content', 'created_at', 'updated_at', )
        read_only_fields = ('article', 'user', )

