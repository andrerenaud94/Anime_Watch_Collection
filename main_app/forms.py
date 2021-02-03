from django import forms
from .models import Episode

class EpisodeForm(forms.ModelForm):
    class Meta:
        model = Episode
        fields = ['number', 'name', 'eptype', 'description', 'link']