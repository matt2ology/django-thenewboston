from .models import Album  # import the Album model from the models.py file.

from django.http import Http404  # raise an Http404 exception.
from django.http import HttpResponse  # basic HTML code or a redirect.
from django.shortcuts import render  # render a template and pass it a context.


def index(request: any) -> HttpResponse:
    """ Returns the index page for the Music app.

    Args:
        request (_type_): this is always the first argument of any view function.

    Returns:
        _type_: HttpResponse object.
    """
    # get all the albums from the database, so we can pass it to the template.
    ALL_ALBUMS: object = Album.objects.all()
    # CONTEXT is a dictionary that maps template variable names to Python objects.
    CONTEXT: dict = {'all_albums': ALL_ALBUMS}
    return render(request, 'music/index.html', CONTEXT)


def detail(request: any, album_id: int) -> HttpResponse:
    """ Returns the details for the album with the given album_id.

    Args:
        request (_type_): this is always the first argument of any view function.
        album_id (int): the id of the album.

    Returns:
        _type_: HttpResponse object.
    """
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
