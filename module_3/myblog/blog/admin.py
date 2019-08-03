from django.contrib import admin
from .models import Author, Blog, Post

admin.site.register(Author)
admin.site.register(Blog)
admin.site.register(Post)