from django.shortcuts import render
from django.shortcuts import redirect, get_object_or_404
from django.views.generic.list import ListView
from django.views.generic import TemplateView, ListView, DetailView
from django.views import View
from song.models import Song, Artist
# Create your views here.



class HomeList(ListView):
    model = Artist
    context_object_name = "all_artist"
    template_name = "song/index.html"


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["all_songs"] = Song.objects.filter(status=1)
        return context
    
class AllSong(ListView):
    model = Song
    context_object_name = "all_song"
    template_name = "song/all-song.html"
    
class PlaySong(DetailView):
    template_name='song/detail.html'
    context_object_name = 'song'
    
    
    def get_object(self, queryset=None):
        pk = self.kwargs.get(self.pk_url_kwarg)
        song = get_object_or_404(Song, pk=pk)
        return song
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        song = self.get_object()
        context["all_songs"] = Song.objects.filter(status=True, artist=song.artist)
        return context
  
        
        
class ChoiceArtist(View):
    def get(self, request, artist_id):
        artist = get_object_or_404(Artist, pk= artist_id)
        songs = Song.objects.filter(artist=artist.id)
        context = {'all_songs':songs}
        return render (request , 'song/songs.html',context)
    
class Searchview(View):
    def get(self,request):
        songs = Song.objects.filter(status=1)
        q = request.GET.get('q')
        songs = songs.filter(title__icontains=q)
        context = {'all_song':songs}
        return render (request , "song/all-song.html",context)
