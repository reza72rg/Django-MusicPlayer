from django.urls import path, include
from song.views import HomeList, PlaySong, ChoiceArtist, AllSong

app_name = "song"

urlpatterns = [
    # Task list view
    path("", HomeList.as_view(), name="home"),
    path('all_song/', AllSong.as_view(), name='all_song'),
    path('artist-choice/<int:artist_id>/', ChoiceArtist.as_view(), name='artist_choice'),
    path('play_song/<int:song_id>/', PlaySong.as_view(), name='play_song'),
]