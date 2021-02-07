from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('about/', views.about, name='about'),
    path('anime/', views.anime_index, name='anime_index'),
    path('anime/<int:anime_id>', views.anime_detail, name='anime_detail'),
    
    #FAVORITE PATHS
    path('anime/<int:anime_id>/assoc_anime/', views.assoc_anime, name='assoc_anime'),
    path('anime/<int:anime_id>/<int:episode_id>/assoc_episode/', views.assoc_episode, name='assoc_episode'),

    #UN-FAVORITE PATHS
    path('users/profile/<int:user_id>/<int:anime_id>', views.unassoc_anime, name='unassoc_anime'),

    #CRUD PATHS (ANIME)
    path('anime/add_anime', views.add_anime, name='add_anime'),
    path('anime/<int:anime_id>/edit/', views.edit_anime, name='edit_anime'),
    path('anime/<int:anime_id>/delete/', views.delete_anime, name='delete_anime'),

    #CRUD PATHS (EPISODE)
    path('anime/<int:anime_id>/add_episode', views.add_episode, name='add_episode'),
    path('anime/<int:anime_id>/<int:episode_id>/edit/', views.edit_episode, name='edit_episode'),
    path('anime/<int:anime_id>/<int:episode_id>/delete/', views.delete_episode, name='delete_episode'),

    #AUTH PATHS
    path('users/profile/', views.profile, name='profile')
]