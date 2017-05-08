from django.db import models

class Photo(models.Model):

    photo_text = models.CharField(max_length = 10000)
    photo_image = models.FileField()

    def __str__(self):
        return self.photo_text;
