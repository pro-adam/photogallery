from django.urls import path
from . import views


urlpatterns = [
    path('',views.home,name='home'),
    path('photos/<int:album_id>/',views.photos,name='photos'),
    path('accounts/signup/',views.signup,name='signup'),
]
