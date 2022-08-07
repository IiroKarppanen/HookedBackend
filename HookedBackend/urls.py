from django.contrib import admin
from django.urls import path, include
from core.views import movie, movie_detail
from django.views.generic import TemplateView

urlpatterns = [
    path("movies/", movie, name="movie"),
    path("movies/<int:pk>/", movie_detail, name="movie-detail"),
    path('api/', include('accounts.urls')),

]
