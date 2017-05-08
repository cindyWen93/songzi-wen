from django.db import models

class Song(models.Model):
    song_title = models.CharField(max_length = 250)
    song_logo = models.CharField(max_length = 1000)
    """song_file = models.FileField(default = None);"""

    def __str__(self):
        return self.song_title;
