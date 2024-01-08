from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views import View
from song.models import Song, Artist
# Create your views here.



class HomeList(ListView):
    model = Artist
    context_object_name = "all_artist"
    template_name = "song/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_songs"] = Song.objects.all()
        return context
    
class AllSong(ListView):
    model = Song
    context_object_name = "all_song"
    template_name = "song/all-song.html"
    
class PlaySong(View):
    def get(self, request, song_id):
        song = get_object_or_404(Song, pk= song_id)
        context = {'song':song}
        return render (request , 'song/detail.html',context)
        
class ChoiceArtist(View):
    def get(self, request, artist_id):
        artist = get_object_or_404(Artist, pk= artist_id)
      
        songs = Song.objects.filter(artist=artist.id)
       
        context = {'all_songs':songs}
        return render (request , 'song/songs.html',context)