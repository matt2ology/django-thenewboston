from django.http import HttpResponse  # basic HTML code or a redirect.
from .models import Album  # import the Album model from the models.py file.


def index(request: any) -> HttpResponse:
    """ Returns the index page for the Music app.

    Args:
        request (_type_): this is always the first argument of any view function.

    Returns:
        _type_: HttpResponse object.
    """
    ALL_ALBUMS: object = Album.objects.all()
    HTML: str = ''
    for album in ALL_ALBUMS:
        # URL pattern: /music/album_id/
        URL = '/music/' + str(album.id) + '/'
        # HTML <a> href Attribute
        # <a href="https://www.w3schools.com">Visit W3Schools</a>
        HTML += 'Album Title :<a href="' + URL + '">' + album.album_title + '</a><br>'
    return HttpResponse(HTML)


def detail(request: any, album_id: int) -> HttpResponse:
    """ Returns the details for the album with the given album_id.

    Args:
        request (_type_): this is always the first argument of any view function.
        album_id (int): the id of the album.

    Returns:
        _type_: HttpResponse object.
    """
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
