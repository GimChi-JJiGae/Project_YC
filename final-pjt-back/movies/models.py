from django.db import models
from django.contrib.postgres.fields import ArrayField
from django.conf import settings
from django.core.validators import MaxValueValidator, MinValueValidator
# Create your models here.

class Genre(models.Model):
    name = models.TextField()


class Movie(models.Model):
    title = models.TextField()
    original_id = models.IntegerField()
    original_title = models.TextField()
    overview = models.TextField()
    genres = models.ManyToManyField(Genre)
    poster_path = models.TextField()
    vote_average = models.FloatField(validators=[MinValueValidator(0), MaxValueValidator(10)])
    vote_count = models.IntegerField(validators=[MinValueValidator(0)])
    release_date = models.TextField()
    runtime = models.IntegerField(validators=[MinValueValidator(0)])
    popularity = models.FloatField(validators=[MinValueValidator(0)])
    adult = models.BooleanField()
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movies')


class MovieComment(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="movie_comments")
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="comments")
    content = models.TextField()
    rank = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    like_movie_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_movie_comments')
    hate_movie_comment_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='hate_movie_comments')