from django.db import models

# Create your models here.


class movies(models.Model):

    character = models.CharField(max_length=50)
    movie_name = models.CharField(max_length=50)
    year = models.IntegerField()
    rating = models.IntegerField()
    villian = models.CharField(max_length=50)
    phase = models.IntegerField()

    def __str__(self):
        return self.character