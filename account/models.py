from django.utils.translation import gettext_lazy as _
from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    username = models.CharField(_("username"), unique=True, max_length=40)
    image = models.ImageField(upload_to='images/profile', null=True, blank=True)
    email = models.EmailField(_('email address'), unique=True)
    phone = models.CharField(max_length=11, null=True, blank=True)
    first_name = models.CharField(_("first name"), max_length=150, blank=True)
    last_name = models.CharField(_("last name"), max_length=150, blank=True)

    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email', 'first_name', 'last_name']

    def get_absolute_url(self):
        return reverse('home:main')

    def __str__(self):
        return self.first_name

