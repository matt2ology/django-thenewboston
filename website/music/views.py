from django.http import HttpResponse  # basic HTML code or a redirect.


def index(request):
    """Returns the homepage for the Music app.

    Args:
        request (_type_): this is always the first argument of any view function.

    Returns:
        _type_: HttpResponse object.
    """
    return HttpResponse("<h1>This is the Music app homepage.</h1>")
