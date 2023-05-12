from django.urls import path
from . import views

urlpatterns = [
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='login'),
    path('signout', views.signout, name='logout'),
    path('profilePage', views.profilePage, name='profile'),
    path('editProfile/<pk>', views.editProfile, name='edit-Profile')
]
