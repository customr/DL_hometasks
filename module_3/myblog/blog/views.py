from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from blog.models import Author, Blog, Post


def index(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request, 'blog/index.html', context)

def blog(request, blog_id):
	blog = get_object_or_404(Blog, pk=blog_id)
	context = {'blog': blog}
	return render(request, 'blog/blog_detail.html', context)

def get_blogs(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request, 'blog/blog.html', context)

def post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	context = {'post': post}
	return render(request, 'blog/post_detail.html', context)

def get_posts(request):
	posts = Post.objects.all()
	context = {'posts': posts}
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

def archive(request):
	posts_qs = Post.objects.all().order_by('-date_published')
	context = {'posts_qs': posts_qs}
	return render(request, 'blog/archive.html', context)