"""
URL configuration for website project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from django.urls import include  # allows referencing other URLconfs.

urlpatterns = [
    # q: whats the difference between path and re_path?
    # a: a path is a string, a re_path is a regex.
    # q: whats the difference between a URL Resolver and a URL Pattern?
    # a: a URL Resolver is a regex, a URL Pattern is a string.
    path('admin/', admin.site.urls),
    path('music/', include('music.urls')),
]
