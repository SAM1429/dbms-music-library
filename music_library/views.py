from django.shortcuts import render,redirect,get_object_or_404
from music_library.models import Album,Song, Playlist, Artist
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from .forms import UpdateProfileForm
from django.contrib.auth.forms import UserChangeForm
from django.contrib.auth import update_session_auth_hash


# Create your views here.

# def favourite (request):
#     if request.method == 'POST':
#        for value in request.POST['n']:
#         song_name = Song.objects.filter(song_title__contains = value)
#         return HttpResponse(song_name)
#         # if song_name.is_favourite == False:
#         #     song_name.is_favourite = True
#         # song_name.save()


# def like_song(request, pk):
#     #return HttpResponse("hello")
#     return HttpResponseRedirect(reverse('home'))


@login_required

# def update_profile(request):
#     if request.method == 'POST':
#         form = UpdateUserForm(request.POST, instance=request.user)
#         if form.is_valid():
#             user = form.save()
#             update_session_auth_hash(request, user) # to update the session  auth hash
#             return redirect('update_profile')
#     else:
#         form = UpdateUserForm(instance=request.user)
#     return render(request, 'update_profile.html', {'form': form})
def update_profile(request):
    if request.method == 'POST':
        form = UpdateProfileForm(request.POST)
        if form.is_valid():
            user = request.user
            user.username= form.cleaned_data['username']
            user.email = form.cleaned_data['email']
            password = form.cleaned_data.get('password')
            password_confirm = form.cleaned_data.get('password_confirm')
            if password and password == password_confirm:
                user.set_password(password)
                user.save()
                update_session_auth_hash(request, user)
            return redirect('update_profile')
    else:
        form = UpdateProfileForm(initial={
            'username': request.user.username,
            'first_name': request.user.first_name,
            'last_name': request.user.last_name,
            'email': request.user.email
        })
    return render(request, 'update_profile.html', {'form': form})




def artist_profile(request, id):

    artist = Artist.objects.get(artist_id__contains = id)
    # a_name = Artist.objects.get(album__album_name=searched)


    return render(request, 'artist_profile.html', {'artist':artist})


def delete_song(request, id):
    song = get_object_or_404(Playlist, id = id, user=request.user)
    song.delete()
    return redirect('playlist')

def logout(request):
    auth.logout(request)
    return redirect('/')

def playlist(request):


    # if request.user.is_authenticated:
    #     user = request.user
    #     if request.method == 'POST':
    #         searched = request.POST['searched']
    #         search_word = Song.objects.filter(song_title__contains = searched)
    #         if search_word:
    #             for n in search_word:
    #                 song = n
    #             playlist_instance = Playlist(song_id=song, user=user,  audio_file = song.file_type)
    #             playlist_instance.save()
    #             playlistData = Playlist.objects.filter(user=user)
    #             return render(request, 'playlist.html', {'PlaylistData':playlistData, 'user': user})
    #         else:
    #             playlistData = Playlist.objects.filter(user=user)
    #             return render(request, 'playlist.html', {'user': user, 'error': 'Song not found'})
    #     else:
    #         playlistData = Playlist.objects.filter(user=user)
    #         return render(request, 'playlist.html', {'PlaylistData':playlistData, 'user': user})
    # else:
    #     return redirect('login')



#---------------------------------------old 2 code-----------------------------------------------------------
    #to get the user's id cause we have related that as a foriegn key
    user_id = request.user.id
    print(user_id)

    #need to check if the request is a post otherwise page only wont open as initially we dont have any form of request!

    if request.method == 'POST':
        searched = request.POST['searched']

        if not searched:
            return redirect('playlist')

        search_word = Song.objects.filter(song_title__contains = searched)
        

        if not search_word:
            return redirect('playlist')


        #to check if the word actually exits in the Song database

        if(search_word):
            #getting the title and song_id attributes from the Song object
            for n in search_word:
                title = n.song_title
                songId = n.song_id
                
                #!! ------------------need to change playlist model to include the song file also hehe--------------
                songFile = n.file_type
            
            #creating the various attributes of the playlist instance
            playlistData = Playlist.objects.all()
            playlits={
            'PlaylistData': playlistData
                    }
        #we are checking here for unique entry
        
            if Playlist.objects.filter(song_title=title, user=user_id).exists():
                return render(request, 'playlist.html',{'PlaylistData':playlistData, 'user': request.user})

                


            playlist_instance = Playlist(song_title=title, user_id = user_id, audio_file = songFile)

            #saving the instance to the database!
            playlist_instance.save()

            print(title)
            return render(request, 'playlist.html',{'PlaylistData':playlistData, 'user': request.user})


        else:
            playlistData = Playlist.objects.all()
            playlits={
            'PlaylistData': playlistData
                    }
            print('sorry not found')
            return render(request, 'playlist.html', {'user': request.user, 'PlaylistData':playlistData})

    else:

        playlistData = Playlist.objects.all()
        playlits={
            'PlaylistData': playlistData
                    }

        if(playlistData):
            return render(request, 'playlist.html', {'PlaylistData':playlistData, 'user': request.user})

        else:

            return render(request, 'playlist.html', {'user': request.user})


    

def search(request):
    if request.method == 'POST':
        searched = request.POST['searched']

        if not searched:
            return redirect('home')

        search_word = Song.objects.filter(album_name__album_name__contains = searched)

        if not search_word:
            return redirect('search')

        album_cover = Album.objects.filter(album_name__contains = searched)
        a_name = Artist.objects.get(album__album_name=searched)
        return render(request, 'search.html', {'searched':searched, 'search_word': search_word, 'album_cover':album_cover, 'a_name': a_name})
    else:
        return render(request, 'search.html')




    
def home(request):
    AlbumsData = Album.objects.all()
    albums={
        'AlbumsData': AlbumsData
    }
    return render(request, 'home.html',{'AlbumsData':AlbumsData})
    

def index(request):
    
    return render(request, 'index.html')
    