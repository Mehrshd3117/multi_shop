from .models import Category


def Category_navbar(request):
    category = Category.objects.all()
    return {
        'category': category
    }