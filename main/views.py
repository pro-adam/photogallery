from django import forms
from django.shortcuts import redirect, render
from django.db.models import Count
from . models import Album,Photos
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from . forms import  AlbumForm,PhotoForm

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


@login_required
def dashboard(request):
    totalAlbum = Album.objects.filter(user=request.user).count()
    totalPhotos = Photos.objects.filter(album__user=request.user).count()
    data = Album.objects.all()
    context = {
        'totalAlbum':totalAlbum,
        'totalPhotos':totalPhotos
    }
    return render(request,'dashboard.html',context)

@login_required
def user_album_list(request):
    data = Album.objects.annotate(total_photos=Count('photos')).filter(user=request.user)
    return render(request,'user-album-list.html',{'data':data})

@login_required
def add_album(request):
    msg = ''
    form = AlbumForm()
    if request.method == 'POST':
        form = AlbumForm(request.POST,request.FILES)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = request.user
            formSave.save()
            msg='form submitted successfully!'
            return redirect('user_album_list')
    return render(request,'add-album.html',{'form':form,'msg':msg})

@login_required
def update_album(request,id):
    msg = ''
    album = Album.objects.get(id=id)
    form = AlbumForm(instance=album)
    if request.method == 'POST':
        form = AlbumForm(request.POST,request.FILES)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = request.user
            formSave.save()
            msg='form submitted successfully!'
            #return redirect('user_album_list')
    return render(request,'update-album.html',{'form':form,'msg':msg})


@login_required
def delete_album(request,id):
    Album.objects.get(id=id).delete()
    return redirect('user_album_list')


@login_required
def user_photo_list(request,id):
    album = Album.objects.get(id=id)
    photos = Photos.objects.filter(album=album)
    return render(request,'user-photo-list.html',{'photos':photos})


@login_required
def delete_photo_list(request,album_id,photo_id):
	Photos.objects.filter(id=photo_id).delete()
	return redirect('/user-photo-list/'+str(album_id))

@login_required
def add_photo(request):
    msg = ''
    form = PhotoForm()
    if request.method == 'POST':
        form = PhotoForm(request.POST,request.FILES)
        if form.is_valid():
            formSave = form.save(commit=False)
            formSave.user = request.user
            formSave.save()
            msg = "photo added successfully"
            return redirect(request,'user-photo-list')
    context = {
        'form':form,
        'msg':msg
    }
    return render(request,'add-photo.html',context)    