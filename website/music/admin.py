from django.contrib import admin

# we need this so we can register the Album and Song model with the admin site
from .models import Album, Song

# this is how we register the Album model with the admin site so we can see it in the admin site
admin.site.register(Album)
admin.site.register(Song)
