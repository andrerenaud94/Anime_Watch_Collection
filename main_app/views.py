from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Anime, Episode, Profile
from .forms import *
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required

# Create your views here.
def profile(request):
    context = {
        'current_user': request.user
    }
    return render(request, 'users/profile.html', context)





def home(request):
    return render(request, 'home.html')





def about(request):
    return render(request, 'about.html')





def anime_index(request):
    anime = Anime.objects.all()
    context = {
        'anime_data': anime,
        'current_user': request.user
    }
    return render(request, 'anime/index.html', context)





def add_anime(request):
    if request.method == 'POST':
        form = AnimeForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('anime_index')
    else: 
        form = AnimeForm()
        context = {
            'form': form
        }
        return render(request, 'anime/add.html', context)




def edit_anime(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    if request.method == 'POST':
        form = AnimeForm(request.POST, instance=anime)
        if form.is_valid():
            form.save()
            return redirect('anime_detail', anime_id=anime_id)
    else:
        form = AnimeForm(instance=anime)
        context = {
            'form': form,
            'anime': anime
        }
    return render(request, 'anime/edit.html', context)




def delete_anime(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    if request.method == 'POST':
        anime.delete()
    return redirect('anime_index')




def delete_episode(request, anime_id, episode_id):
    episode = Episode.objects.get(id=episode_id)
    if request.method == 'POST':
        episode.delete()
    return redirect('anime_detail', anime_id=anime_id)




def edit_episode(request, anime_id, episode_id):
    episode = Episode.objects.get(id=episode_id)
    anime = Anime.objects.get(id=anime_id)
    if request.method == 'POST':
        form = EpisodeForm(request.POST, instance=episode)
        if form.is_valid():
            form.save()
            return redirect('anime_detail', anime_id=anime_id)
    else:
        form = EpisodeForm(instance=episode)
        context = {
            'form': form,
            'anime': anime,
            'episode': episode
        }
    return render(request, 'episode/edit.html', context)




def anime_detail(request, anime_id):
    anime = Anime.objects.get(id=anime_id)
    episode_form = EpisodeForm()

    context = {
        'anime_data': anime,
        'episode_form': episode_form,
        'current_user': request.user
    }
    return render(request, 'anime/detail.html', context)





def add_episode(request, anime_id):
    form = EpisodeForm(request.POST)

    if form.is_valid():
        new_episode = form.save(commit=False)
        new_episode.anime_id = anime_id
        new_episode.save()
    
    return redirect('anime_detail', anime_id=anime_id)




def assoc_anime(request, anime_id):
    user = request.user
    user.profile.animes.add(anime_id)
    return redirect('anime_detail', anime_id=anime_id)




def unassoc_anime(request,user_id, anime_id):
    user = request.user
    user.profile.animes.remove(anime_id)
    return redirect('profile')




def assoc_episode(request, anime_id, episode_id):
    user = request.user
    user.profile.episodes.add(episode_id)
    return redirect('anime_detail', anime_id=anime_id)