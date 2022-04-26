from django.db import models


class Titles(models.Model):
    anime = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    chapters = models.IntegerField()
