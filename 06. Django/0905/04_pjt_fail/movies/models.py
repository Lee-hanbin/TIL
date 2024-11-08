from django.db import models

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    audience = models.PositiveIntegerField()
    release_date = models.DateField()
    genre = models.CharField(max_length=30)
    score = models.FloatField()
    poster_url = models.TextField()
    description = models.TextField()