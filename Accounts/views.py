from django.shortcuts import render


def account_information(request):
    return render(request, "account_information.html")

def address_book(request):
    return render(request, "address_book.html")

def contact_information(request):
    return render(request, "contact_information.html")

def forgot_password(request):
    return render(request, "forgot_password.html")

def login(request):
    return render(request, "login.html")

def register(request):
    return render(request, "register.html")
