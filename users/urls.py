from django.urls import path

from . import views

# USERS URLS

app_name = 'users'

urlpatterns = [
    path('register', views.register, name = 'register'),
    path('profile/', views.profile, name = 'profile'),
]
