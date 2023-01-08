from django.db import models
from django.template.defaultfilters import slugify


class BlogCategory(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Category"
        verbose_name_plural = "Blog Categories"


class BlogAuthor(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Blog Author"
        verbose_name_plural = "Blog Authors"


class Blog(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField(unique=True, null=True, blank=True)
    author_id = models.ForeignKey(BlogAuthor, on_delete=models.CASCADE)
    category_id = models.ManyToManyField(BlogCategory, related_name='blogs')
    description = models.TextField()
    cover_image = models.ImageField(upload_to = "blog_images")
    view_count = models.PositiveIntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    update_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    class Meta:
        verbose_name = "Blog"
        verbose_name_plural = "Blogs"


class BlogComment(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField(max_length=100, blank=True)
    comment = models.TextField(max_length=700)
    created_at = models.DateTimeField(auto_now_add=True)
    blog_id = models.ForeignKey(Blog, on_delete=models.CASCADE, null=True, related_name='comments')

    def __str__(self):
        return f"{self.name}'s comment"

    class Meta:
        verbose_name = "Blog Comment"
        verbose_name_plural = "Blog Comments"

