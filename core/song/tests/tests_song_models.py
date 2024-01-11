from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from song.models import Song, Artist, Category
from yourapp.views import HomeList  # Import the HomeList view from your app

class TestSongModels(TestCase):
    def test_create_song_with_valid_data(self):
        artist = Artist.objects.create(name='test')
        category = Category.objects.create(name="test")
        author = User.objects.create(username="test", password="123456789ab")
        song = Song.objects.create(
            title="test",
            author=author,
            artist=artist,
            category=category,
        )
        self.assertEqual(resolve(url).func.view_class,HomeList)

    