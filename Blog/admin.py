from django.contrib import admin
from .models import Blog, BlogAuthor, BlogCategory, BlogComment

admin.site.register([Blog, BlogAuthor, BlogCategory, BlogComment])
