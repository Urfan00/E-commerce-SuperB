from django.shortcuts import render, redirect
from django.db.models import Avg, Count, Q
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import CreateView, DetailView, ListView
from .forms import ReviewForm
from .models import Image, ProductCategory, ProductReview, ProductVersion, Products
from Core.models import Logo



class ProductListView(ListView):
    model = Products
    template_name = "product-list.html"
    context_object_name = 'products'
    paginate_by = 3

    def get_context_data(self, **kwargs):
        context = super(ProductListView, self).get_context_data(**kwargs)
        context['categories'] = ProductCategory.objects.filter(is_navbar = "True").all()
        context['sub_categories'] = ProductCategory.objects.filter(is_navbar = "False").all()
        context['logos'] = Logo.objects.all()
        context['sizes'] = ProductVersion.objects.values_list("size_id__name", flat=True).distinct().values('size_id__name').annotate(count = Count('size_id__name')).order_by('size_id__name')
        context['colors'] = ProductVersion.objects.values_list("color_id__name", flat=True).distinct().values('color_id__name').annotate(count = Count('color_id__name')).order_by('color_id__name')
        return context

    def get_queryset(self):
        order = self.request.GET.get('order')
        category = self.request.GET.get('category')
        s_category1 = self.request.GET.get('s_category1')
        subcategory = self.request.GET.get('subcategory')
        size = self.request.GET.get('size')
        color = self.request.GET.get('color')
        minPrice= self.request.GET.get('minPrice')
        maxPrice= self.request.GET.get('maxPrice')

        if (category and s_category1 and subcategory):
            self.queryset = ProductVersion.objects.filter(product_id__category_id__category_name=subcategory, product_id__category_id__parent_category__category_name=s_category1, product_id__category_id__parent_category__parent_category__category_name = category)
        elif (category and s_category1):
            self.queryset = ProductVersion.objects.filter(product_id__category_id__parent_category__category_name=s_category1, product_id__category_id__parent_category__parent_category__category_name = category)
        elif (category):
            self.queryset = ProductVersion.objects.filter(product_id__category_id__parent_category__parent_category__category_name = category)
        elif color:
            self.queryset = ProductVersion.objects.filter(color_id__name = color).all()
        elif size:
            self.queryset = ProductVersion.objects.filter(size_id__name = size).all()
        elif order:
            if order == 'A-Z':
                self.queryset = ProductVersion.objects.order_by('product_id__title').all()
            elif order == 'Z-A':
                self.queryset = ProductVersion.objects.order_by('-product_id__title').all()
            elif order == 'lowtohigh':
                self.queryset = ProductVersion.objects.order_by('product_id__price').all()
            elif order == 'hightolow':
                self.queryset = ProductVersion.objects.order_by('-product_id__price').all()
            elif order == 'newest':
                self.queryset = ProductVersion.objects.order_by('-product_id__created_at').all()
        elif (minPrice and maxPrice):
            self.queryset = ProductVersion.objects.filter(product_id__price__range=(minPrice, maxPrice)).all()
        elif minPrice:
            self.queryset = ProductVersion.objects.filter(Q(product_id__price__gte = minPrice))
        elif maxPrice:
            self.queryset = ProductVersion.objects.filter(Q(product_id__price__lte = maxPrice))
        else:
            self.queryset = ProductVersion.objects.order_by('created_at').all()
        return self.queryset


class ProductDetailView(LoginRequiredMixin, CreateView, DetailView):
    model = Products
    form_class = ReviewForm
    template_name = 'product-detail.html'
    context_object_name = 'product'

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        product_count = ProductVersion.objects.get(product_id=self.object)
        product_count.read_count += 1
        product_count.save()
        return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super(ProductDetailView, self).get_context_data(**kwargs)
        context['images'] = Image.objects.filter(product_version_id__product_id = self.object).all()
        context['version'] = ProductVersion.objects.filter(product_id = self.object).all()
        context['reviews'] = ProductReview.objects.filter(product_version_id__product_id__slug = self.kwargs.get('slug')).all()[:3]
        context['logos'] = Logo.objects.all()
        context['related'] = ProductVersion.objects.filter(product_id__category_id = self.object.category_id).exclude(product_id__slug = self.kwargs.get('slug')).all()
        return context

    def form_valid(self, form, *args, **kwargs):
        form.instance.product_version_id = ProductVersion.objects.get(product_id__slug = self.kwargs.get('slug'))
        form.instance.save()

        self.object = self.get_object()
        product = ProductVersion.objects.get(product_id=self.object)
        product.review_count += 1

        rate_average = ProductReview.objects.filter(product_version_id__product_id__slug = self.kwargs.get('slug')).aggregate(average=Avg('product_rate'))
        product.rate_avg = rate_average['average'] * 20
        product.save()

        return redirect("product_detail", slug = self.kwargs.get('slug'))


class SearchResultsView(LoginRequiredMixin, ListView):
    model = Products
    template_name = 'search.html'
    context_object_name = 'products'

    def get_queryset(self):
        query = self.request.GET.get('search')
        if query:
            products=ProductVersion.objects.filter(Q(product_id__title__icontains=query)).all()
        else:
            products=ProductVersion.objects.all()
        return products
