from django.contrib import admin
from .models import Anime
from .models import Episode

# Register your models here.
admin.site.register(Anime)
admin.site.register(Episode)