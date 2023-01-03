from django.shortcuts import render



def error(request):
    return render(request, "404error.html")

def about_us(request):
    return render(request, "about_us.html")

def contact_us(request):
    return render(request, "contact_us.html")

def faq(request):
    return render(request, "faq.html")

def index(request):
    return render(request, "index.html")
