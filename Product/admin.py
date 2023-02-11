from django.contrib import admin
from .models import Color, Image, ProductCategory, ProductReview, ProductVersion, Products, Size

admin.site.register([Color, Image, ProductCategory, ProductReview, ProductVersion, Products, Size])
