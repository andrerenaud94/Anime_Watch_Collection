from django.db import models

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    episodes = models.IntegerField()
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.name


