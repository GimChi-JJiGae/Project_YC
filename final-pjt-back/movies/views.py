from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework_jwt.authentication import JSONWebTokenAuthentication
from rest_framework.permissions import IsAuthenticated
from django.shortcuts import render, get_object_or_404, get_list_or_404
from django.contrib.auth import get_user_model
from rest_framework import status

from .models import Movie, Genre, MovieComment
from .serializers import MovieSerializer, MovieCommentSerializer, GenreSerializer

@api_view(['GET'])
def home(request):
    if request.method == 'GET':
        movies = get_list_or_404(Movie)
        serializer = MovieSerializer(movies, many=True)
        return Response(serializer.data) 

@api_view(['GET'])
def get_genres(request):
    if request.method == 'GET':
        genres = get_list_or_404(Genre)
        serializer = GenreSerializer(genres, many=True)
        return Response(serializer.data)

@api_view(['GET'])
def getrandomMovies(request, genre_id):
    genre = get_object_or_404(Genre, id=genre_id)
    movies = genre.movie_set.order_by('?')[:20]
    serializer = MovieSerializer(movies, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def movie_detail(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.method == 'GET':
        serializer = MovieSerializer(movie)
        return Response(serializer.data)

@api_view(['GET'])
def movie_comment_list(request):
    comments = get_list_or_404(MovieComment)
    serializer = MovieCommentSerializer(comments, many=True)
    return Response(serializer.data)

@api_view(['GET', 'PUT', 'DELETE'])
def movie_detail_comments(request, pk):
    print("댓글조회 도착")
    #comment = get_object_or_404(MovieComment, pk=comment_pk)
    
    if request.method == 'GET':
        comments = get_list_or_404(MovieComment, movie_id=pk)
        print(comments)
        serializer = MovieCommentSerializer(comments, many=True)
        return Response(serializer.data)

    elif request.method == 'PUT':
        comment = get_object_or_404(MovieComment, pk=pk)
        serializer = MovieCommentSerializer(comment, data=request.data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response(serializer.data)

    elif request.method == 'DELETE':
        comment = get_object_or_404(MovieComment, pk=pk)
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

@api_view(['POST'])
def movie_comment_create(request, movie_pk):
    print("댓글생성 도착!")
    movie = get_object_or_404(Movie, pk=movie_pk)
    serializer = MovieCommentSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save(movie=movie, user=request.user)
        return Response(serializer.data, status=status.HTTP_201_CREATED)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    if request.user in movie.like_users.all():
        movie.like_users.remove(request.user)
        is_liked = False
    else:
        movie.like_users.add(request.user)
        is_liked = True
    context = {
        'is_liked' : is_liked,
        'likes_count': movie.like_users.count()
    }
    return Response(context)

@api_view(['GET'])
def get_likes(request, movie_pk):
    movie = get_object_or_404(Movie, pk=movie_pk)
    context = {
        'likes_count': movie.like_users.count()
    }
    return Response(context)


@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_like(request, movie_comment_pk):
    comment = get_object_or_404(MovieComment, pk=movie_comment_pk)
    if request.user in comment.like_movie_comment_users.all():
        comment.like_movie_comment_users.remove(request.user)
        is_liked = False
    else:
        comment.like_movie_comment_users.add(request.user)
        is_liked = True
    context = {
        'is_liked' : is_liked,
        'likes_count': comment.like_movie_comment_users.count()
    }
    return Response(context)

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def comment_hate(request, movie_comment_pk):
    comment = get_object_or_404(MovieComment, pk=movie_comment_pk)
    if request.user in comment.hate_movie_comment_users.all():
        comment.hate_movie_comment_users.remove(request.user)
        is_hated = False
    else:
        comment.hate_movie_comment_users.add(request.user)
        is_hated = True
    context = {
        'is_hated' : is_hated,
        'hates_count': comment.hate_movie_comment_users.count()
    }
    return Response(context)