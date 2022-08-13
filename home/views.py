from django.shortcuts import render
from django.views import View
from product.models import Product, Category


class Home(View):
    def get(self, request):
        product = Product.objects.filter(available=True)
        categories = Category.objects.all()
        return render(request, 'home/index.html', {
            'product': product,
            'categories': categories
        })

