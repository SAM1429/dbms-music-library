from django.db import models 
from django.contrib.auth.models import User

# from django.db.models import CharField
# from django_case_insensitive_field import CaseInsensitiveFieldMixin

# Create your models here.

class Artist(models.Model):
    artist_id = models.IntegerField(primary_key= True, null= False)
    artist_name = models.CharField(max_length=100)
    artist_pic = models.FileField(upload_to='images')

    def __str__(self):
        return self.artist_name



class Album(models.Model):
    album_id = models.IntegerField(primary_key=True, null=False)
    artist_id = models.ForeignKey(Artist, on_delete=models.CASCADE)
    album_name = models.CharField(max_length=500)
    album_logo = models.ImageField(upload_to='images')

    def __str__(self):
        return self.album_name


class Song(models.Model):
   
    file_type = models.FileField(upload_to='mp3')
    song_title = models.CharField(max_length=250)
    song_id = models.IntegerField(primary_key=True)
    album_name = models.ForeignKey(Album, on_delete=models.CASCADE)


    def __str__(self):
        return self.song_title

class Playlist(models.Model):
    user = models.ForeignKey(User,on_delete= models.CASCADE)
    song_title = models.CharField(max_length=100)
    song_id = models.ManyToManyField(Song, related_name='playlists', blank=True)
    audio_file = models.FileField(upload_to='mp3')

    

    # class Meta:
    #     unique_together = ('song_title', 'user_id')


   



