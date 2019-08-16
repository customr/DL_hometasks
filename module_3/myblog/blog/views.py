from django.shortcuts import render, get_object_or_404, reverse
from django.http import HttpResponse, HttpResponseRedirect
from django.utils import timezone
from django.views.generic import edit
from django.db.models import F

from blog.models import Blog, Post, Comment
from blog.forms import UserCreationForm


class RegisterFormView(edit.FormView):
    form_class = UserCreationForm
    success_url = "success"
    template_name = "registration/registration.html"

    def form_valid(self, form):
        form.save()
        return super(RegisterFormView, self).form_valid(form)


class NewBlog(edit.CreateView):
	model = Blog
	template_name = 'blog/new_blog.html'
	fields = ['author', 'name']


class NewPost(edit.CreateView):
	model = Post
	template_name = 'blog/new_post.html'
	fields = ['blog', 'author', 'topic', 'title', 'text']


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

def register_success(request):
	return render(request, 'registration/registration_success.html', {})


#`````````````````````````````ACTIONS```````````````````````````````````
def like_post(request, post_id):
	post = get_object_or_404(Post, pk=post_id)

	try:
		post.liked_users[post_id]

	except Exception:
		post.liked_users[post_id] = {}

	finally:	
		if request.META['REMOTE_ADDR'] not in post.liked_users[post_id].values():
			post.liked_users[post_id][f'{post.id}'] = request.META['REMOTE_ADDR']
			Post.objects.filter(pk=post_id).update(rating=F('rating') + 1)

	return HttpResponseRedirect(reverse('blog:post', args=(post.id, )))

def like_comment(request, comment_id):
	comment = get_object_or_404(Comment, pk=comment_id)
	try: 
		comment.liked_users[comment_id]
	
	except Exception:
		comment.liked_users[comment_id] = {}

	finally:
		if request.META['REMOTE_ADDR'] not in comment.liked_users[comment_id].values():
			comment.liked_users[comment_id][f'{comment.id}'] = request.META['REMOTE_ADDR']
			Comment.objects.filter(pk=comment_id).update(rating=F('rating') + 1)

	return HttpResponseRedirect(reverse('blog:post', args=(comment.post.id, )))

def post_comment(request):
	pass

def unlike_post(request):
	pass

def unlike_comment(request):
	pass

def logout(request):
	return render(request, 'registration/logout.html', {})