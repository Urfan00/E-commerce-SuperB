from django.urls import path
from .views import checkout, checkout_billing_info, shopping_cart, wishlist


urlpatterns = [
    path('checkout_billing_info/', checkout_billing_info, name = "checkout_billing_info"),
    path('checkout/', checkout, name = "checkout"),
    path('shopping_cart/', shopping_cart, name = "shopping_cart"),
    path('wishlist/', wishlist, name = 'wishlist')
]