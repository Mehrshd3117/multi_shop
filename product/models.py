from django.urls import reverse
from django.db import models
from django.utils.html import format_html
from django.utils.text import slugify


class Category(models.Model):
    parent = models.ForeignKey('self', default=None, null=True, blank=True, on_delete=models.CASCADE, related_name="children", verbose_name="زیر دسته")
    name = models.CharField(max_length=255, verbose_name="نام دسته")
    image = models.ImageField(upload_to="images/category", verbose_name="عکس")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="عنوان url")

    class Meta:
        verbose_name = "دسته بندی"
        verbose_name_plural = "دسته بندی ها"

    def save(self, *args, **kwargs):
        self.slug = slugify(self.name)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.name

    def show_image(self):
        if self.image:
            return format_html(f'<img src="{self.image.url}" width="50px" height="50px">')
        return format_html('<h3 style="color: red">تصویر ندارد</h3>')
    show_image.short_description = " تصویر"


class Product(models.Model):
    title = models.CharField(max_length=255, verbose_name='نام محصول')
    category = models.ForeignKey(Category, verbose_name="دسته بندی", related_name="category", on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=5, decimal_places=2, verbose_name="قیمت")
    discount = models.CharField(max_length=255, verbose_name="تخفیف")
    description = models.TextField(verbose_name="توضیحات")
    slug = models.SlugField(max_length=255, unique=True, verbose_name="عنوان url")
    available = models.BooleanField(default=True, verbose_name="موجود")
    is_active = models.BooleanField(default=True, verbose_name='فعال,غیر فعال')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='ایجاد شده در تاریخ')
    updated = models.DateTimeField(auto_now=True, verbose_name='به روز رسانی شده در تاریخ')

    class Meta:
        verbose_name = "محصول"
        verbose_name_plural = "محصول ها"
        ordering = ('created_at',)

    def get_absolute_url(self):
        return reverse('product:detail', kwargs={'slug': self.slug})

    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        return super().save(*args, **kwargs)

    def __str__(self):
        return self.title
