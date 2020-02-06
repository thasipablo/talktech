"""talktech URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.contrib.auth import views as auth_views
from django.urls import include, path

from django.conf import settings
from django.conf.urls.static import static

from talktech.urls import auth_views

from . import views

urlpatterns = [
    path('', views.home, name = 'home'),
    path('adminer/', admin.site.urls),
    path('about/', views.about, name = 'about'),
    
    path('login', auth_views.LoginView.as_view(template_name = 'users/login.html'), name = 'login'),
    path('logout', auth_views.LogoutView.as_view(template_name = 'users/logout.html'), name = 'logout'),
    
    path('users/', include('users.urls')),
    path('blog/', include('blog.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)    
