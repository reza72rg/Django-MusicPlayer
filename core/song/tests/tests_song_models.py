from django.test import TestCase
from django.urls import reverse, resolve
from django.contrib.auth.models import User
from song.models import Song, Artist, Category


class TestSongModels(TestCase):
    def setUp(self):
        self.artist = Artist.objects.create(name='test')
        self.category_obj = Category.objects.create(name="test")
        self.author = User.objects.create(username="test", password="123456789ab")
    def test_create_song_with_valid_data(self):
        song = Song.objects.create(
            title="test",
            author=self.author,
            artist=self.artist,)
        song.category.set([self.category_obj])
        self.assertTrue(Song.objects.filter(pk=song.id).exists())
        self.assertEqual(song.author.username,"test")

    