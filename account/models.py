from django.db import models
from django.urls import reverse
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    email = models.EmailField(unique=True, verbose_name='ایمیل')
    phone = models.BigIntegerField(verbose_name='شماره تلفن همراه', null=True)

    def get_absolute_url(self):
        return reverse('home:main')







