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
]
