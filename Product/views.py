from django.shortcuts import render


def product_detail(request):
    return render(request, "product-detail.html")

def product_list(request):
    return render(request, "product-list.html")

def quick_view(request):
    return render(request, "quick_view.html")
