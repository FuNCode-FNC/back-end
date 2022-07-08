from django.contrib import admin
from django.urls import path, include
from main import views

urlpatterns = [
    path("", views.main_page, name="main_page"),
    path("films_genres/", views.films_genres, name="films_genres"),
    path("moderator/", views.moderator, name="moderator"),
    path("recovery-page/", views.recovery_page, name="recovery_page"),
    path("sign-in-page/", views.sign_in_page, name="sign_in_page"),
    path("sign-up-email/", views.sign_up_email, name="sign_up-email"),
]
