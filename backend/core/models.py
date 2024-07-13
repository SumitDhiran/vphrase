from django.db import models

# Create your models here.

class Movie(models.Model):
    movie = models.CharField(max_length=500, null=True, blank=True)
    year = models.IntegerField(null=True, blank=True)
    genre = models.CharField(max_length=255, null=True, blank=True)
    rating = models.FloatField(null=True, blank=True)
    one_line = models.TextField(null=True, blank=True)
    stars = models.TextField(null=True, blank=True)
    votes = models.FloatField(null=True, blank=True)
    runtime = models.FloatField(null=True, blank=True)
    gross = models.FloatField(null=True, blank=True)



    def __str__(self) -> str:
        return str(self.movie)
