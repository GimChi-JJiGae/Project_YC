from django.db import models
from django.contrib.auth.models import AbstractUser


# Create your models here.
class User(AbstractUser):
    email = models.EmailField(unique=True, help_text='EMAIL')
    username = models.CharField(max_length=30, unique=True)
    password = models.CharField(max_length=20)
    image = models.ImageField(blank=True)

    SEX_CHOICES = {
        ('male', 'Male'),
        ('female', 'Female'),
    }

    age = models.CharField(max_length=20)
    sex = models.CharField(max_length=10, choices=SEX_CHOICES, null=False, default="male")

    followers = models.ManyToManyField('self', symmetrical=False, related_name='followings')
    
    def __str__(self):
        return self.username