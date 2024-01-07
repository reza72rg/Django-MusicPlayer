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
    

    
class PlaySong(View):
    def get(self, request, song_id):
        song = get_object_or_404(Song, pk= song_id)
        context = {'song':song}
        return render (request , 'song/song.html',context)
        
