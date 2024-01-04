from django.urls import path, include
from song.views import Songlist

app_name = "song"

urlpatterns = [
    # Task list view
    path("", Songlist.as_view(), name="song-list"),
]