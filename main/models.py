from django.db import models
from django.contrib.auth.models import User
from django.utils.html import mark_safe

class Album(models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    album_image = models.ImageField(upload_to='album_img/',null=True)
    title = models.CharField(max_length=100)

    def __str__(self):
        return self.title

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'%(self.album_image.url))


class Photos(models.Model):
    album = models.ForeignKey(Album,on_delete=models.CASCADE,null=True)
    alt_txt = models.CharField(max_length=100)
    image   = models.ImageField(upload_to='photos/')   

    class Meta:
        verbose_name_plural = 'Photos'   

    def __str__(self):
        return self.alt_txt

    def image_tag(self):
        return mark_safe('<img src="%s" width="80"/>'%(self.image.url))
