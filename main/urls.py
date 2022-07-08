from django.urls import path, include,re_path
from . import views
from django.contrib.auth import views as auth_views



urlpatterns = [

    path('api/v1/logIn',views.logIn),
    path('api/v1/signUp', views.signUp),
    path('api/v1/logOut',views.logOut),
    path('api/v1/resetPass', views.passRecovery),
    path('api/v1/changePass', views.change_pass),


    path('', views.main),
    path('activate/<slug:uidb64>/<slug:token>/',views.activate, name='activate'),
    path('reset/<slug:uidb64>/<slug:token>/',views.set_recovery_pass, name='reset'),
    path('login/', views.loginning),
    path('signup/', views.signupping),
    path('signup/email/', views.signup_email),
    path('profile/', views.profile),
    path('profile/password/change/', views.change_pass_view),
    path('password/recovery/', views.recovery_page),
    path('password/recovery/done', views.recovery_page_email)

]