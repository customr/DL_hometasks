from django.contrib import admin
from django.urls import path, include

from blog import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index-page'),
	path('blog/<int:blog_id>/', views.blog, name='blog'),
	path('blogs/', views.get_blogs, name='blogs'),
	path('post/<int:post_id>/', views.post, name='post'),
	path('posts/', views.get_posts, name='posts'),
	path('author/<int:author_id>/', views.author, name='author'),
	path('authors/', views.get_authors, name='authors'),
	path('archive/', views.archive, name='archive'),
]