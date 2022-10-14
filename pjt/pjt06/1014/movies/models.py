from django.db import models

# Create your models here.

class Movie(models.Model):
    title = models.CharField(max_length=20)
    description = models.TextField()
    user_id = models.IntegerField()

class Comment(models.Model):
    # movie = models.ForeignKey()
    content = models.CharField(max_length=100)
    movie_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return self.content