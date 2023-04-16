from django.urls import path, re_path
from . import views

app_name: str = 'music'  # this is the namespace for the Music app.

urlpatterns = [
    # path('', views.index, name='index'), # the homepage for the Music app.
    re_path(r'^$', views.index, name='index'),  # pattern : /music/
    # q: how do you do path with regex?
    # a: https://docs.djangoproject.com/en/4.2/topics/http/urls/#example
    path('<int:album_id>/', views.detail, name='detail'), # pattern : /music/album_id/
]
