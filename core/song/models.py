from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from django.utils.translation import gettext as _
from django.db.models.fields.files import ImageFieldFile
from PIL import Image
from io import BytesIO
from django.core.files import File
from django.conf import settings
from django.utils.safestring import mark_safe
from django.utils.text import slugify
from .tools import UploadToPathAndRename
def get_image_field(self):
    output = []
    for k, v in self.__dict__.items():
        if isinstance(v, ImageFieldFile):
            output.append(k)
    return output


class MainModel(models.Model):
    create_date = models.DateTimeField(auto_now_add=True, blank=True, null=True, verbose_name=_("create date"))
    modify_date = models.DateTimeField(auto_now=True, blank=True, null=True, verbose_name=_("modify date"))
    is_active = models.BooleanField(default=True, verbose_name=_("is active"))

    def save(self, *args, **kwargs):
        image_fields = get_image_field(self)
        if image_fields:
            for i in image_fields:
                if hasattr(self, i) and isinstance(getattr(self, i), ImageFieldFile):
                    image = Image.open(getattr(self, i).file)
                    image_io = BytesIO()
                    image_extension = getattr(self, i).name.rpartition(".")[-1].upper()
                    image_extension = "JPEG" if image_extension == "JPG" else image_extension
                    image.save(image_io, image_extension, quality=60)
                    new_image = File(image_io, name=getattr(self, i).name)
                    setattr(self, i, new_image)
        self.full_clean()
        super().save(*args, **kwargs)

    class Meta:
        abstract = True

class Category(models.Model):
    name = models.CharField(max_length=255)
    def __str__(self):
        return self.name


class Artist(MainModel):
    image = models.ImageField(upload_to=UploadToPathAndRename("artist"),default='artist/default.jpg')
    name = models.CharField(max_length=255)
    
    def __str__(self):
        return self.name
    
class Song(models.Model):
    image = models.ImageField(upload_to=UploadToPathAndRename("song"),default='song/default.jpg')
    title = models.CharField(max_length=255)
    author = models.ForeignKey(User,on_delete=models.SET_NULL,null=True, related_name='song_author')
    artist = models.ForeignKey(Artist, on_delete= models.CASCADE, related_name="relate_song")
    audio = models.FileField(blank=True,null=True)
    slug = models.SlugField(null=True,blank=True,unique=True)
    category = models.ManyToManyField(Category)
    count_view = models.IntegerField(default=0)
    status =models.BooleanField(default= False)
    created_date = models.DateTimeField(auto_now_add = True)
    updated_data = models.DateTimeField(auto_now= True)
    
    class Meta:
        ordering = ('created_date',)
    def save (self, force_insert = False, force_update=False, using=None,update_fields=None):
        self.slug = slugify(self.title[:5])
        super(Song,self).save()
    def __str__(self):
        return self.title