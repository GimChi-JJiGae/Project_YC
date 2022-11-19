# import re, bcrypt, jwt

from rest_framework import serializers
# from rest_framework.response import Response
# from rest_framework.validators import UniqueTogetherValidator
# from rest_framework_jwt.tokens import jwt
from django.contrib.auth import get_user_model


User = get_user_model()

class UserSerializer(serializers.ModelSerializer):

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

        extra_kwargs = {
            'password': {'write_only': True},
            # 'username': {
            #     'validators': [UniqueValidator(queryset=User.objects.all())]
            # },
            # 'email': {
            #     'validators': [UniqueValidator(queryset=User.objects.all())]
            # },
        }

    # def validate_email(self, obj):
    #     if email_isvalid(obj):
    #         return obj
    #     raise serializers.ValidationError('메일 형식이 올바르지 않습니다.')

    # def validate_password(self, obj):
    #     if password_isvalid(obj):
    #         return hash_password(obj)
    #     raise serializers.ValidationError("비밀번호는 8 자리 이상이어야 합니다.")

    # def validate_username(self, obj):
    #     if username_isvalid(obj):
    #         return obj
    #     raise serializers.ValidationError('닉네임은 한 글자 이상이어야 합니다.')
        
    # def update(self, obj, validated_data):
    #     obj.email = validated_data.get('email', obj.email)
    #     obj.username = validated_data.get('username', obj.username)
    #     obj.password = validated_data.get('password', obj.password)
    #     obj.profile_image_url = validated_data.get('profile_image_url', obj.profile_image_url)
    #     obj.save()
    #     return obj