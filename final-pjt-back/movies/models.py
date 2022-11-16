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
    original_id = models.IntegerField()
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
    
    #likes = models.IntegerField() # 나중에 manytomany로 수정할 예정


class MovieComment(models.Model):
    user_id = models.IntegerField() # N to 1 예정
    movie_id = models.ForeignKey(Movie, on_delete=models.CASCADE)
    content = models.TextField()
    rank = models.IntegerField()