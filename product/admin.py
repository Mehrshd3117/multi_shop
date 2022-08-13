from django.contrib import admin
from . import models


class CategoryAdmin(admin.ModelAdmin):
    list_display = ('__str__', 'show_image','parent')


admin.site.register(models.Category, CategoryAdmin)
admin.site.register(models.Product)

