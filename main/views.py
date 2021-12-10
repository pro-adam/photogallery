from django import forms
from django.shortcuts import render
from django.db.models import Count
from . models import Album,Photos
from django.contrib.auth.forms import UserCreationForm

def home(request):
    data = Album.objects.annotate(total_photos=Count('photos')).all()
    return render(request,'home.html',{'data':data})

def photos(request,album_id):
    album = Album.objects.get(id=album_id)
    data = Photos.objects.filter(album=album)
    return render(request,'photos-list.html',{'data':data,'album':album})

def signup(request):
    msg = ''
    form = UserCreationForm()
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            msg = 'form submitted successfully !'
    return render(request,'registration/signup.html',{'form':form,'msg':msg})