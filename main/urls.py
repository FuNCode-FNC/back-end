from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main_page, name='name_page'),
    path('account/', views.account, name='account'),
    path('filmpage/', views.filmpage, name='filmpage'),
    path('list-of-films/', views.list_of_films, name='list_of_films'),
    path('recovery-new-password/', views.recovery_new_password, name='recovery_new_password'),
    path('change-new-password/', views.change_new_password, name='change_new_password'),
    path('sign-up-page/', views.sign_up_page, name='sign_up_page'),
    path("films_genres/", views.films_genres, name="films_genres"),
    path("moderator/", views.moderator, name="moderator"),
    path("recovery-page/", views.recovery_page, name="recovery_page"),
    path("sign-in-page/", views.sign_in_page, name="sign_in_page"),
    path("sign-up-email/", views.sign_up_email, name="sign_up-email"),
    
    #  need fix
    path('profile',views.profile),
    path('api/v1/logIn',views.logIn),
    path('api/v1/signUp', views.signUp),
    path('api/v1/logOut',views.logOut),
    path('activate/<slug:uidb64>/<slug:token>/',
            views.activate, name='activate'),
]
