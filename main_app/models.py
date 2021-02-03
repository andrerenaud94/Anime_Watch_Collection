from django.db import models

# Create your models here.
class Anime(models.Model):
    name = models.CharField(max_length=250)
    description = models.TextField(max_length=250)
    episodes = models.IntegerField()
    category = models.CharField(max_length=250)

    def __str__(self):
        return self.name


MAIN = (
    ('M', 'Main Story'),
    ('F', 'Filler')
)

class Episode(models.Model):
    number = models.IntegerField()
    name = models.CharField(max_length=250)
    eptype = models.CharField(
        max_length=15,
        choices=MAIN,
        default=MAIN[0]
    )
    description = models.TextField(max_length=250)
    link = models.URLField(max_length=250)

    anime = models.ForeignKey(Anime, on_delete=models.CASCADE)

    def __str__(self):
        return f'Episode {self.number} titled {self.name}'