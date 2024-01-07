from django.urls import path, include
from song.views import HomeList, PlaySong

app_name = "song"

urlpatterns = [
    # Task list view
    path("", HomeList.as_view(), name="home"),
    path('play_song/<int:song_id>/', PlaySong.as_view(), name='play_song'),
]