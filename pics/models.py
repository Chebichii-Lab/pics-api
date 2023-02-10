from django.db import models
from PIL import Image

class User(models.Model):
    name = models.CharField(max_length=200)
    username = models.CharField(max_length=100)
    email = models.EmailField(max_length=300, default='STRING')

    def __str__(self):
        return self.name + ' ' + self.username

class Album(models.Model):
    album_title = models.CharField(max_length=100)
    album_id = models.IntegerField(default=0)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.album_title

class Photo(models.Model):
    album_id = models.ForeignKey(Album, on_delete=models.CASCADE)
    photo_title = models.CharField(max_length=100)
    image_url = models.ImageField('image')

    def __str__(self):
        return self.photo_title