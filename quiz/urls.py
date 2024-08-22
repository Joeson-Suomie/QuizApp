from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LogoutView

urlpatterns = [
    path('', views.home, name='home'),
    path('register/', views.register, name='register'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('profile/', views.profile, name='profile'),
     path('accounts/logged_out/', views.logged_out_view, name='logged_out'),
    path('take_quiz/', views.take_quiz, name='take_quiz'),
]
                               