from django.contrib import admin
from django.urls import path, include
from appBlog.views import *
urlpatterns = [
    path('', start_page, name='start_page'),
    path('<int:id>/', increase_likes_number, name='increase_likes_number'),
    path('add_new_post/', create_new_post, name='create_new_post'),
    path('view_post/<int:id>/', view_post, name='view_post'),
]