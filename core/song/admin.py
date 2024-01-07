from django.contrib import admin
from song.models import Artist, Song, Category
# Register your models here.


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
class SongAdmin(admin.ModelAdmin):
    def get_fields(self, request, obj=None):
        return ["image","title","author","artist","audio","category","count_view","status"]
        
    def get_list_display(self, request):
        return ["title","author","artist","count_view","status"]

