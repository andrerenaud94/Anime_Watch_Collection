from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Anime(models.Model):
    is_featured = models.BooleanField(default=False)
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
    is_featured = models.BooleanField(default=False)
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





class Profile(models.Model):
    is_admin = models.BooleanField(default=False)
    user = models.OneToOneField(User, on_delete=models.CASCADE)

    animes = models.ManyToManyField(Anime, blank=True)
    episodes = models.ManyToManyField(Episode, blank=True)

    def __str__(self):
        return f'{self.user} profile id: {self.user.id}'




class Article(models.Model):
    is_featured = models.BooleanField(default=False)
    image = models.URLField(max_length=250)
    title = models.CharField(max_length=250)
    body = models.TextField()

    def __str__(self):
        return f'Article: {self.title}'