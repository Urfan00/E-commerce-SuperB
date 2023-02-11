from django.urls import path
from .views import ProductDetailView, ProductListView, SearchResultsView


urlpatterns = [
    path('product_list/', ProductListView.as_view(), name = "product_list"),
    path('product_detail/<slug:slug>/', ProductDetailView.as_view(), name = 'product_detail'),
    path('search/', SearchResultsView.as_view(), name = 'search'),
]
