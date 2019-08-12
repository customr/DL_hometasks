from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from django.utils import timezone
from django.views import generic
from django.db.models import F
from django.contrib.auth.forms import UserCreationForm

from blog.models import Author, Blog, Post, Comment


liked_users = {}


class RegisterFormView(generic.edit.FormView):
    form_class = UserCreationForm
    success_url = "accounts/login/"
    template_name = "blog/register.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)

class NewAuthor(generic.edit.CreateView):
	model = Author
	template_name = 'blog/new_author.html'
	fields = ['first_name', 'last_name', 'email', 'date_of_birth']

class NewBlog(generic.edit.CreateView):
	model = Blog
	template_name = 'blog/new_blog.html'
	fields = ['author', 'name']

class NewPost(generic.edit.CreateView):
	model = Post
	template_name = 'blog/new_post.html'
	fields = ['blog', 'author', 'topic', 'title', 'text']

class NewComment(generic.edit.CreateView):
	model = Comment
	template_name = 'blog/post_detail.html'
	fields = ['author', 'post', 'text']

def index(request):
	blogs = Blog.objects.all()
	context = {'blogs': blogs}
	return render(request, 'blog/index.html', context)

def blog(request, blog_name):
	blog = get_object_or_404(Blog, name__iexact=blog_name)
	posts = blog.post_set.all()
	context = {
		'blog': blog,
		'posts': posts
		}
	return render(request, 'blog/blog_detail.html', context)

def post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)
	comments = post.comment_set.all()
	context = {
		'post': post,
		'comments': comments
		}
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
	blogs = Blog.objects.filter(author=author)
	posts = Post.objects.filter(author=author)

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
	blog = Blog.objects.order_by("?").first()
	post = Post.objects.order_by("?").first()
	topic = post.topic
	author = post.author.id
	context = {
		'blog': blog.name,
		'post': post.id,
		'topic': topic,
		'author': author
	}
	return render(request, 'blog/help.html', context)

def like_post(request, post_id):
	global liked_users

	post = get_object_or_404(Post, pk=post_id)

	if request.META['REMOTE_ADDR'] not in liked_users.values():
		comment.rating += 1
		comment.save()
		liked_users[f'{post.id}'] = request.META['REMOTE_ADDR']

	post.comment_set.filter(pk=comment_id).update(rating=F('rating') + 1)
	return HttpResponseRedirect(reverse('blog:post', args=(post.id, )))

def like_comment(request, post_id, comment_id):
	global liked_users

	post = get_object_or_404(Post, pk=post_id)

	if request.META['REMOTE_ADDR'] not in liked_users.values():
		comment.rating += 1
		comment.save()
		liked_users[f'{post.id}'] = request.META['REMOTE_ADDR']

	post.comment_set.filter(pk=comment_id).update(rating=F('rating') + 1)
	return HttpResponseRedirect(reverse('blog:post', args=(post.id, )))

