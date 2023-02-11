from django.db import models
from django.urls import reverse
from django.template.defaultfilters import slugify



class ProductCategory(models.Model):
    category_name = models.CharField(max_length=30)
    is_navbar = models.BooleanField(default=True)
    parent_category = models.ForeignKey("ProductCategory", on_delete=models.CASCADE, related_name="category_parent", null=True, blank=True)

    def __str__(self):
        return self.category_name

    def save(self, *args, **kwargs):
        if self.parent_category == None:
            self.is_navbar = True
        else:
            self.is_navbar = False
        return super().save()

    class Meta:
        verbose_name = "Category"
        verbose_name_plural = "Categories"


class Size(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return f"{self.name} size"


class Color(models.Model):
    name = models.CharField(max_length = 30)

    def __str__(self):
        return self.name


class Products(models.Model):
    discounts = (
        (5, '5'),
        (10, '10'),
        (15, '15'),
        (20, '20'),
        (25, '25'),
        (30, '30'),
        (35, '35'),
        (40, '40'),
        (45, '45'),
        (50, '50')
    )
    cover_image = models.ImageField(upload_to="product_images")
    title = models.CharField(max_length = 50)
    slug = models.SlugField(null=True, blank=True)
    short_descriptions = models.TextField()
    long_descriptions = models.TextField()
    in_sale = models.BooleanField(default=False)
    price = models.FloatField()
    discount = models.IntegerField(choices=discounts, null=True, blank=True)
    new_price = models.FloatField(null=True, blank=True)
    category_id = models.ForeignKey(ProductCategory, on_delete=models.CASCADE, related_name='product_category')
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", kwargs={"slug": self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(f'{self.title}')
        if self.in_sale:
            self.new_price = self.price - self.price*(self.discount/100)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"


class ProductVersion(models.Model):
    in_stock = models.PositiveIntegerField(default=0)
    rate_avg = models.FloatField(default=0)
    review_count = models.PositiveIntegerField(default=0)
    read_count = models.PositiveIntegerField(default=0)
    size_id = models.ManyToManyField(Size, blank=True, related_name="product_size")
    color_id = models.ManyToManyField(Color, blank=True, related_name="product_color")
    product_id = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="product_version")
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.product_id.title}'s version"

    class Meta:
        verbose_name = "Product Version"
        verbose_name_plural = "Product Versions"


class Image(models.Model):
    image = models.ImageField(upload_to="product_images")
    product_version_id = models.ForeignKey(ProductVersion, on_delete=models.CASCADE, related_name='product_version_image')

    def __str__(self):
        return f"{self.product_version_id.product_id.title}'s photo"

    class Meta:
        verbose_name = "Product Image"
        verbose_name_plural = "Product Images"


class ProductReview(models.Model):
    Rates = (
        (1, "20"),
        (2, "40"),
        (3, "60"),
        (4, "80"),
        (5, "100")
    )
    product_rate = models.IntegerField(choices=Rates)
    name = models.CharField(max_length=30)
    surname = models.CharField(max_length=30)
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)
    product_version_id = models.ForeignKey(ProductVersion, on_delete = models.CASCADE, related_name="product_review")

    def __str__(self):
        return f"{self.name}'s reviews"

    class Meta:
        verbose_name = "Product Review"
        verbose_name_plural = "Product Reviews"
