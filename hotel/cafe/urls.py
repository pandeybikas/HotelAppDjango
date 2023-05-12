from django.urls import path
from . import views

urlpatterns = [
    path('cafelist', views.cafelist, name='cafe-list'),
    path('addCafe', views.addCafe, name='add-cafe')
]
