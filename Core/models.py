from django.db import models


class FAQ(models.Model):
    question = models.TextField()
    answer = models.TextField()

    def __str__(self):
        return f'FAQ {self.pk}'

    class Meta:
        verbose_name = "FAQ"
        verbose_name_plural = "FAQs"


class ContactUs(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(max_length=30)
    address = models.TextField(null=True, blank=True)
    phone = models.CharField(max_length=13, null=True, blank=True)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name}'s comment"

    class Meta:
        verbose_name = "Contact Us Comment"
        verbose_name_plural = "Contact Us Comments"


class Logo(models.Model):
    logo = models.ImageField(upload_to='logo_images')

    def  __str__(self):
        return f'logo {self.pk}'
