from django.urls import path
from .views import product_detail, product_list, quick_view


urlpatterns = [
    path('product_detail/', product_detail, name = "product_detail"),
    path('product_list/', product_list, name = "product_list"),
    path('quick_view/', quick_view, name = "quick_view"),
]