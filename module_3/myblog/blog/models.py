import datetime
from django.db import models
from django.utils import timezone
from django.urls import reverse


class Author(models.Model):
	first_name = models.CharField('First name', max_length=25)
	last_name = models.CharField('Last name', max_length=35)
	email = models.CharField('Email', max_length=50)
	date_of_birth = models.DateField('Date of birth', max_length=8)
	rating = models.IntegerField('Rating', default=0)

	def __str__(self):
		return f'#{self.id} {self.first_name} {self.last_name}'

	def get_absolute_url(self):
		return reverse('blog:author', args=[str(self.id)])


class Blog(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	name = models.CharField('Name', max_length=50)
	rating = models.IntegerField('Rating', default=0)

	def __str__(self):
		return f'Blog #{self.id} {self.name}'

	def get_absolute_url(self):
		return reverse('blog:blog', args=[str(self.name)])


class Post(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	topic = models.CharField('Topic', max_length=50)
	title = models.CharField('Title', max_length=50)
	text = models.CharField('Text', max_length=250)
	rating = models.IntegerField('Rating', default=0)
	date_published = models.DateTimeField('Date published', default=timezone.now)

	def was_published_recently(self):
		now = timezone.now()
		return now - datetime.timedelta(days=-1) <= self.date_published <= now

	def __str__(self):
		return f'#{self.id} {self.title}'

	def get_absolute_url(self):
		return reverse('blog:post', args=[str(self.id)])

	@property
	def liked_users(self):
		return self._liked_users

	@liked_users.setter
	def liked_users(self, value):
		assert self._liked_users - value == 1

		self._liked_users = value

	@liked_users.getter
	def liked_users(self):
		return self._liked_users


class Comment(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	post = models.ForeignKey(Post, on_delete=models.CASCADE)
	text = models.CharField('Text', max_length=150)
	rating = models.IntegerField('Rating', default=0)
	date_published = models.DateTimeField('Date published', default=timezone.now)

	@property
	def liked_users(self):
		return self._liked_users

	@liked_users.setter
	def liked_users(self, value):
		assert self._liked_users - value == 1

		self._liked_users = value

	@liked_users.getter
	def liked_users(self):
		return self._liked_users

	def __str__(self):
		return f'Comment {self.id}'