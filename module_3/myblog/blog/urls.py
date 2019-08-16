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
	path('newpost/', views.NewPost.as_view(), name='new_post'),
	path('newblog/', views.NewBlog.as_view(), name='new_blog'),
	#````````````````````````REGISTRATION``````````````````````
	path('register/', views.RegisterFormView.as_view(), name='register'),
	path('register/success/', views.register_success, name='success'),
	path('logout/', views.logout, name='logout'),
	#````````````````````````ACTIONS```````````````````````````
	path('post/comment/create', views.post_comment, name='post_comment'),
	path('post/<int:post_id>/like', views.like_post, name='like_post'),
	path('post/<int:post_id>/unlike', views.unlike_post, name='unlike_post'),
	path('post/comment/<int:comment_id>/like', views.like_comment, name='like_comment'),
	path('post/comment/<int:comment_id>/unlike', views.unlike_comment, name='unlike_comment'),

]