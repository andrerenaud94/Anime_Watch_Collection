from django.shortcuts import render
from django.http import HttpResponse
from .models import Anime

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def anime_index(request):
    return render(request, 'anime/index.html')