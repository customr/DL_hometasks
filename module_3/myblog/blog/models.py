from django.db import models
from django.utils import timezone
from django.urls import reverse


class Author(models.Model):
	first_name = models.CharField('First name', max_length=25)
	last_name = models.CharField('Last name', max_length=35)
	email = models.CharField('Email', max_length=50)
	date_of_birth = models.DateField('Date of birth', max_length=8)

	def __str__(self):
		return f'#{self.id} {self.first_name} {self.last_name}'

	def get_absolute_url(self):
		return reverse('blog:author', args=[str(self.id)])


class Blog(models.Model):
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	name = models.CharField('Name', max_length=50)
	rating = models.IntegerField('Rating', default=0)

	def __str__(self):
		return self.name

	def get_absolute_url(self):
		return reverse('blog:blog', args=[str(self.name)])


class Post(models.Model):
	blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
	author = models.ForeignKey(Author, on_delete=models.CASCADE)
	topic = models.CharField('Topic', max_length=50)
	title = models.CharField('Title', max_length=50)
	text = models.CharField('Text', max_length=250)
	created_date = models.DateTimeField('Date created', default=timezone.now)
	date_published = models.DateTimeField('Date published', default=timezone.now)

	def publish(self):
		self.date_published = timezone.now()
		self.save()

	def __str__(self):
		return f'#{self.id} {self.title}'

	def get_absolute_url(self):
		return reverse('blog:post', args=[str(self.id)])
