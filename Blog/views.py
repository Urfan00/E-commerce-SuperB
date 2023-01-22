from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from .forms import BlogCommentForm
from .models import Blog, BlogAuthor, BlogCategory, BlogComment


class BlogListView(LoginRequiredMixin, ListView):
    model = Blog
    template_name = "blog.html"
    context_object_name = 'blogs'

    def get_context_data(self, **kwargs):
        context = super(BlogListView, self).get_context_data(**kwargs)
        context["categories"] = BlogCategory.objects.all()
        context["authors"] = BlogAuthor.objects.all()
        context["most_popular_post"] = Blog.objects.order_by('-view_count').all()[:4]
        return context

    def get_queryset(self):
        category = self.request.GET.get("category")
        author = self.request.GET.get("author")
        if category:
            self.queryset = Blog.objects.filter(category_id__category_slug = category).order_by("-created_at").all()
        elif author:
            self.queryset = Blog.objects.filter(author_id__author_slug = author).order_by("-created_at").all()
        else:
            self.queryset = Blog.objects.order_by("-created_at").all()
        return self.queryset


class BlogDetailView(LoginRequiredMixin, DetailView, CreateView):
    model = Blog
    template_name = 'blog_detail.html'
    form_class = BlogCommentForm
    context_object_name = 'blog'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        blog_view = Blog.objects.get(title = self.object)
        blog_view.view_count += 1
        blog_view.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(BlogDetailView, self).get_context_data(**kwargs)
        context["categories"] = BlogCategory.objects.all()
        context["authors"] = BlogAuthor.objects.all()
        context["most_popular_post"] = Blog.objects.order_by('-view_count').all()[:4]
        context["reviews"] = BlogComment.objects.filter(blog_id__slug = self.kwargs.get('slug')).all()[:10]
        return context

    def form_valid(self, form, *args, **kwargs):
        form.instance.blog_id = Blog.objects.get(slug = self.kwargs.get('slug'))
        form.instance.save()
        return redirect("blog_detail", slug = self.kwargs.get('slug'))
