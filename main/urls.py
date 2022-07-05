from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.index),
    path('profile',views.profile),
    path('api/v1/logIn',views.logIn),
    path('api/v1/signUp', views.signUp),
    path('api/v1/logOut',views.logOut),
    path('activate/<slug:uidb64>/<slug:token>/',
            views.activate, name='activate'),

]