from django.contrib import admin
from . models import Album,Photos


class AlbumAdmin(admin.ModelAdmin):
    list_display = ('title','image_tag')
admin.site.register(Album,AlbumAdmin)

class PhotosAdmin(admin.ModelAdmin):
    list_display = ('alt_txt','image_tag')
admin.site.register(Photos,PhotosAdmin)
