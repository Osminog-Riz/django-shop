from django.shortcuts import render

from products.models import Category, Product, Image


def index(request):
    return render(request, 'index.html')


def categories_list(request):
    categories = Category.objects.all()
    return render(request, 'category_list.html', {'categories': categories})


def product_list(request, pk):
    category = Category.objects.get(id=pk)
    products = Product.objects.filter(category=category)
    return render(request, 'product_list.html', {'category': category, 'products': products})


def product_info(request, pk):
    product = Product.objects.get(id=pk)
    images = Image.objects.filter(product=product)
    return render(request, 'product.html', {'product': product, 'images': images})
