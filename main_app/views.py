from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Anime
from .forms import EpisodeForm

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    anime = Anime.objects.all()
    context = {'anime_data': anime}
    return render(request, 'anime/index.html', context)

def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    episode_form = EpisodeForm()

    context = {
        'anime_data': anime,
        'episode_form': episode_form
    }
    return render(request, 'anime/detail.html', context)

def add_episode(request, anime_id):
    form = EpisodeForm(request.POST)

    if form.is_valid():
        new_episode = form.save(commit=False)
        new_episode.anime_id = anime_id
        new_episode.save()
    
    return redirect('anime_detail', anime_id=anime_id)