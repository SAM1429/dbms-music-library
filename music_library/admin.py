from django.contrib import admin
from .models import Album, Song,Playlist, Artist


admin.site.register(Song)
admin.site.register(Album)
admin.site.register(Playlist)
admin.site.register(Artist)

