from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'), 
    path('hotelDetail/<slug>', views.hotelDetail, name='hotel-detail'),
    path('hotelDetail/<slug>/bookRoom', views.bookRoom, name='book-room'),
    path('hotelDetail/<slug>/hotelMenu', views.hotelMenu, name='hotel-menu'),
    path('editMenu/<pk>', views.editMenu, name='edit-menu'),
    path('hotelList', views.hotelList, name='hotel-list'),
    path('cityDetail/<slug>', views.cityDetail, name='city-detail')
]
