from django.db import models


class Message(models.Model):
    name = models.CharField(max_length=40, verbose_name="نام")
    subject = models.CharField(max_length=100, verbose_name="موضوع")
    email = models.EmailField(verbose_name="ایمیل")
    message = models.TextField(verbose_name="پیام")

    def __str__(self):
        return self.subject

    class Meta:
        verbose_name = "پیام"
        verbose_name_plural = "پیام ها"



