from django.db import models
from django.forms import  ModelForm
from . models import Album,Photos

class AlbumForm(ModelForm):
    class Meta:
        model = Album
        fields = ('title','album_image')


class PhotoForm(ModelForm):
    class Meta:
        model = Photos
        fields = ('album','image','alt_txt')
