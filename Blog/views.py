from django.shortcuts import render


def blog(request):
    return render(request, "blog.html")

def blog_detail(request):
    return render(request, "blog_detail.html")
