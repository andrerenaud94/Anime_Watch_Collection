from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime

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
    context = {'anime_data': anime}
    return render(request, 'anime/detail.html', context)