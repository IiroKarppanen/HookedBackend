from django.db import models
from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, BaseUserManager

# Create your models here.

class Movies(models.Model):
    movie_id = models.CharField(max_length=10, blank=True)
    title = models.CharField(max_length=100, blank=True)
    start_year = models.CharField(max_length=6, blank=True)
    end_year = models.CharField(max_length=6, blank=True)
    age = models.CharField(max_length=15, blank=True)
    plot = models.CharField(max_length=5000, blank=True)
    revenue = models.CharField(max_length=20, blank=True)
    rating = models.CharField(max_length=5, blank=True)
    runtime = models.CharField(max_length=10, blank=True)
    votes = models.CharField(max_length=20, blank=True)
    genres = models.CharField(max_length=50, blank=True)
    kind = models.CharField(max_length=10, blank=True)
    ep_count = models.CharField(max_length=5, blank=True)
    cast = models.CharField(max_length=1000, blank=True)
    image_url = models.CharField(max_length=3000, blank=True)
    
    def __str__(self):
        return self.title