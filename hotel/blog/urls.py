from django.urls import path 
from . import views

urlpatterns = [
    path('blogList', views.blogList, name='blog-list'),
    path('blogDetail/<slug>', views.blogDetail, name='blog-detail'),
    path('blogDetail/<slug>/addComment', views.addComment, name='add-comment'),
    path('commentdelete/<pk>', views.commentdelete, name="comment-delete"),
    path('addBlog', views.addBlog, name='add-blog'),
   
]
