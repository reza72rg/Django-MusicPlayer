from django.contrib import admin
from song.models import Artist, Song, Category
# Register your models here.
from django_summernote.admin import SummernoteModelAdmin

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["name"]
        
    def get_list_display(self, request):
        return ["name"]
  
@admin.register(Artist)
class ArtistAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["image","name"]
        
    def get_list_display(self, request):
        return ["name"]
  
@admin.register(Song)
class SongAdmin(SummernoteModelAdmin):
    def get_fields(self, request, obj=None):
        return ["image","title","author","artist","audio","category","count_view","status","lyric"]
        
    def get_list_display(self, request):
        return ["title","author","artist","count_view","status"]
    def get_list_filter(self, request, filters=None):
        return ["artist"]
    def get_summernote_fields (self,request):
        return ["lyric"]



