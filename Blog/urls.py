from django.urls import path
from .views import blog_detail, blog


urlpatterns = [
    path('blog_detail/', blog_detail, name = "blog_detail"),
    path('blog/', blog, name = "blog")
]
