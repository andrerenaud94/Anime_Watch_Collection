from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('anime/', views.anime_index, name='anime_index'),
    path('anime/<int:anime_id>', views.anime_detail, name='anime_detail'),
    path('anime/<int:anime_id>/add_episode', views.add_episode, name='add_episode')
]