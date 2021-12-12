from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('photos/<int:album_id>/',views.photos,name='photos'),
    path('accounts/signup/',views.signup,name='signup'),
    path('dashboard/',views.dashboard,name='dashboard'),
    path('user-album-list/',views.user_album_list,name='user_album_list'),
    path('add-album/',views.add_album,name='add_album'),
    path('add-photo/',views.add_photo,name='add_photo'),
    path('update-album/<int:id>/',views.update_album,name='update_album'),
    path('delete-album/<int:id>/',views.delete_album,name='delete_album'),
    path('user-photo-list/<int:id>/',views.user_photo_list,name='user-photo-list'),
    path('delete-photo-list/<int:album_id>/<int:photo_id>/',views.delete_photo_list,name='delete-photo-list'),
]
