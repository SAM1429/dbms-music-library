from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home', views.home, name = 'home'),
    path('search', views.search, name = 'search'),
    path('playlist', views.playlist, name = 'playlist'),
    path('logout', views.logout, name = 'logout'),
    path('update_profile', views.update_profile, name = 'update_profile'),
    path('delete_song/<int:id>', views.delete_song, name = 'delete_song'),
    path('artist_profile/<int:id>', views.artist_profile, name = 'artist_profile'),

    # path('like_song/<int:pk>', views.like_song, name = 'like_song'),
    # path('favourite', views.favourite, name = 'favourite')

]

