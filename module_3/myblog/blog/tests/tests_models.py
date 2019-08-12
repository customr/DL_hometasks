import datetime

from django.test import TestCase
from django.utils import timezone

from blog.models import Author, Post, Blog, Comment


def create_author(**kw):
	authors = Author.objects.all()

	if len(authors) == 0 or len(kw) != 0:
		return Author('Test', 'Test', 'test@mail.ru', '1999-02-02', **kw)
	else:
		return authors[0]

def create_blog(**kw):
	blogs = Blog.objects.all()

	if len(blogs) == 0 or len(kw) != 0:
		return Blog(create_author(), 'test', **kw)
	else:
		return blogs[0]

def create_post(**kw):
	posts = Post.objects.all()

	if len(posts) == 0 or len(kw) != 0:
		return Post(create_blog(), create_author(), 'test', 'test', 'test', **kw)
	else:
		return posts[0]


class PostTest(TestCase):

	def test_was_published_recently(self):
		author = create_author()
		blog = create_blog()

		post_old = create_post(date_published=timezone.now() + datetime.timedelta(days=-30))
		post = create_post()
		post_future = create_post(date_published=timezone.now() + datetime.timedelta(days=30))

		self.assertEqual(post_old.was_published_recently(), False)
		self.assertEqual(post.was_published_recently(), True)
		self.assertEqual(post_future.was_published_recently(), False)
