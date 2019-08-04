from django.contrib import admin
from django.urls import path, include

from blog import views

app_name = 'blog'
urlpatterns = [
	path('', views.index, name='index-page'),
	path('blog/<str:blog_name>/', views.blog, name='blog'),
	path('post/<int:post_id>/', views.post, name='post'),
	path('posts/', views.get_posts, name='posts'),
	path('posts/topic/<str:topic>', views.get_posts, name='posts_topic'),
	path('author/<int:author_id>/', views.author, name='author'),
	path('authors/', views.get_authors, name='authors'),
	path('help/', views.help, name='help'),
]