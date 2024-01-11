from django.test import TestCase, SimpleTestCase
from django.urls import reverse, resolve
from song.views import HomeList, PlaySong
# Create your tests here.
class TestUrls(SimpleTestCase):
    def test_song_home_urls_resolve(self):
        url = reverse("song:home")
        self.assertEqual(resolve(url).func.view_class,HomeList)

    def test_song_play_song_urls_resolve(self):
        url = reverse("song:play_song",kwargs={'pk':1})
        self.assertEqual(resolve(url).func.view_class,PlaySong)
