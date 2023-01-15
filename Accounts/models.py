from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(_('email address'), unique=True)
    bio = models.TextField('Bio', null=True, blank=True)
    image = models.ImageField(upload_to = 'users_avatars', null=True, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', ]

    def __str__(self):
        return self.username

    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
