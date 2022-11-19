from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404
from django.contrib.auth import get_user_model
from rest_framework import status
from .serializers import UserSerializer


@api_view(['POST'])
def signup(request):
	#1-1. Client에서 온 데이터를 받아서
    password = request.data.get('password')
    password_confirmation = request.data.get('passwordConfirmation')
		
	#1-2. 패스워드 일치 여부 체크
    if password != password_confirmation:
        return Response({'error': '비밀번호가 일치하지 않습니다.'}, status=status.HTTP_400_BAD_REQUEST)
		
	#2. UserSerializer를 통해 데이터 직렬화
    serializer = UserSerializer(data=request.data)
    
	#3. validation 작업 진행 -> password도 같이 직렬화 진행
    if serializer.is_valid(raise_exception=True):
        user = serializer.save()
        #4. 비밀번호 해싱 후 
        user.set_password(request.data.get('password'))
        user.save()
    # password는 직렬화 과정에는 포함 되지만 → 표현(response)할 때는 나타나지 않는다.
        return Response(serializer.data, status=status.HTTP_201_CREATED)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def my_profile(request):

    user = get_object_or_404(get_user_model(), username=request.data.get('username'))
    serializer = UserSerializer(user)

    return Response(serializer.data)



@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def profile(request, username):
    user = get_object_or_404(get_user_model(), username=request.data.get('username'))
    serializer = UserSerializer(user)
    return Response(serializer.data)


@api_view(['GET'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def users(request):
    users = get_user_model().objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def follow(request, my_pk, user_pk):
    person = get_object_or_404(get_user_model(), pk=user_pk)
    me = get_object_or_404(get_user_model(), pk=my_pk)
    if person != me:
        if me.followings.filter(pk=person.pk).exists():
        # if user in person.followers.all():
            me.followings.remove(person)
            following = False
            # followed가 더 좋은 표현인 듯
        else:
            me.followings.add(person)
            following = True
        print(me.followings.filter(pk=person.pk))
        return Response(following)


@api_view(['POST'])
@authentication_classes([JSONWebTokenAuthentication])
@permission_classes([IsAuthenticated])
def users_info(request):
    # print(request.data)
    users = request.data.get('users')
    movies = []
    for user in users:
        user = get_object_or_404(get_user_model(), pk=user)
        serializer = UserSerializer(user)
        # print(serializer.data)
        like_movies = serializer.data.get('like_movies')
        for movie in like_movies:
            if movie not in movies:
                movies.append(movie)
    
    return Response(movies)