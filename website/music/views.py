from django.http import HttpResponse  # basic HTML code or a redirect.


def index(request):
    """Returns the homepage for the Music app.

    Args:
        request (_type_): this is always the first argument of any view function.

    Returns:
        _type_: HttpResponse object.
    """
    return HttpResponse("<h1>This is the Music app homepage.</h1>")


def detail(request: any, album_id: int) -> HttpResponse:
    """ Returns the details for the album with the given album_id.

    Args:
        request (_type_): this is always the first argument of any view function.
        album_id (int): the id of the album.

    Returns:
        _type_: HttpResponse object.
    """
    return HttpResponse("<h2>Details for Album id: " + str(album_id) + "</h2>")
