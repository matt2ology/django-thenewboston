from django.db import models

class Album(models.Model):
    """
    Album model that has the following attributes:
    `artist`, `album_title`, `genre`, and `album_logo`.
    """
    # The primary key is automatically created by Django and is called id.
    # But we can also create our own primary key by adding the following line:
    # `id = models.AutoField(primary_key=True)`
    artist = models.CharField(max_length=250)
    album_title = models.CharField(max_length=500)
    genre = models.CharField(max_length=250)
    # URL to album logo image file
    album_logo = models.CharField(max_length=1000)

    def __str__(self):
        """This is what will be displayed in the admin page
        for each album object created in the database
        (instead of Album object (1), Album object (2), etc.)

        Returns:
            [string] -- [artist name - album title]
        """
        return self.album_title + ' - ' + self.artist


class Song(models.Model):
    """
    Song model that is linked to an album model via a
    foreign key relationship (one to many) and has the following attributes:
    `file_type`, `song_title`, and `is_favorite` (boolean).
    """
    # on_delete=models.CASCADE means that if the album is deleted, all songs
    # associated with that album will be deleted as well (cascading delete)
    # foreign key relationship (one to many) with Album model
    # (one album can have many songs)
    album = models.ForeignKey(Album, on_delete=models.CASCADE)
    file_type = models.CharField(max_length=10)  # mp3, wav, etc.
    song_title = models.CharField(max_length=250)
    is_favorite = models.BooleanField(default=False)

    def __str__(self):
        """This is what will be displayed in the admin page
        for each song object created in the database
        (instead of Song object (1), Song object (2), etc.)

        Returns:
            [string] -- [song title]
        """
        return self.song_title
