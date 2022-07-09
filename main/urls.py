from django.contrib import admin
from django.urls import path, include
from . import views

urlpatterns = [
    path("", views.main_page, name='name_page'),
    path('account/', views.account, name='account'),  # add key (id)
    path('filmpage/', views.filmpage, name='filmpage'),  # add key (id)
    path("film/<int:pk>", views.film_detail, name='film_detail'),
    path('list-of-films/', views.list_of_films, name='list_of_films'),  # write for loop in template

    # доступна только через почту (не трогать)
    path('recovery-new-password/', views.recovery_new_password, name='recovery_new_password'),
    # доступна только через почту (не трогать)
    path('change-new-password/', views.change_new_password, name='change_new_password'),
    # доступна только через почту (не трогать)
    path("recovery-page/", views.recovery_page, name="recovery_page"),

    path('recovery-email/', views.recovery_page_email),

    path('sign-up-page/', views.sign_up_page, name='sign_up_page'),
    path("films_genres/", views.films_genres, name="films_genres"),
    path("moderator/", views.moderator, name="moderator"),  # доступна только модератору
    path("sign-in-page/", views.sign_in_page, name="sign_in_page"),
    path("sign-up-email/", views.sign_up_email, name="sign_up-email"),

    path('api/v1/logIn', views.logIn),
    path('api/v1/signUp', views.signUp),
    path('api/v1/logOut', views.logOut),
    path('api/v1/resetPass', views.passRecovery),
    path('api/v1/changePass', views.change_pass),
    path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    path('reset/<slug:uidb64>/<slug:token>/', views.set_recovery_pass, name='reset'),

    path('about', views.main_page, name='about')
    # path('', views.main),
    # path('activate/<slug:uidb64>/<slug:token>/', views.activate, name='activate'),
    # path('login/', views.loginning),
    # path('signup/email/', views.signup_email),
    # path('profile/', views.profile),
    # path('profile/password/change/', views.change_pass),
    # path('password/recovery/', views.recovery_page),
    # path('password/recovery/done', views.recovery_page_email)
]
