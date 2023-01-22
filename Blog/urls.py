from django.urls import path
from .views import BlogDetailView, BlogListView


urlpatterns = [
    path('blog/', BlogListView.as_view(), name = "blog"),

    path('blog_detail/<slug:slug>', BlogDetailView.as_view(), name = "blog_detail"),
]
