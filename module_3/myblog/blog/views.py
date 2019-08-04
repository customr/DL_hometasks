import datetime
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone

from blog.models import Author, Blog, Post


def index(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request, 'blog/index.html', context)

def blog(request, blog_name):
	blog = get_object_or_404(Blog, name__iexact=blog_name)
	posts = Post.objects.all().filter(blog=blog)
	context = {
		'blog': blog,
		'posts': posts
		}
	return render(request, 'blog/blog_detail.html', context)

def post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)


def get_posts(request, topic=None):
	posts = Post.objects.all()
	if topic is not None:
		posts = posts.filter(topic__iexact=topic)
	context = {
		'posts': posts,
		'topic': topic
		}
	return render(request, 'blog/post.html', context)

def author(request, author_id):
	author = get_object_or_404(Author, pk=author_id)
	blogs = Blog.objects.all().filter(author=author)
	posts = Post.objects.all().filter(author=author)

	context = {
		'author': author,
		'posts': posts,
		'blogs': blogs
		}
	return render(request, 'blog/author_detail.html', context)

def get_authors(request):
	authors = Author.objects.all()
	context = {'authors': authors}
	return render(request, 'blog/author.html', context)

def help(request):
	return render(request, 'blog/help.html', {})