from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path("", views.main_page),
    path("film/<int:pk>", views.film_detail, name='film_detail'),
]
