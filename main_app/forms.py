from django import forms
from .models import *

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['number', 'name', 'eptype', 'description', 'link']

class AnimeForm(forms.ModelForm):
    class Meta:
        model = Anime
        fields = ['name', 'description', 'episodes', 'category']