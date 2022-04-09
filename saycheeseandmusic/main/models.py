from distutils.command.upload import upload
from django.db import models


class Song(models.Model):
    song_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=2000)
    singer = models.CharField(max_length=2000)
    album = models.CharField(max_length=2000)
    song_img = models.ImageField(upload_to='images')
    song_file = models.FileField(upload_to='images')
    duration = models.CharField(max_length=20)
    paginate_by = 2

    def __str__(self):
        return self.name


