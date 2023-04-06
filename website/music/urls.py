from django.urls import path, re_path
from . import views

urlpatterns = [
    # path('', views.index, name='index'), # the homepage for the Music app.
    re_path(r'^$', views.index, name='index'),
    # q: how do you do path with regex?
    # a: https://docs.djangoproject.com/en/4.2/topics/http/urls/#example
]
