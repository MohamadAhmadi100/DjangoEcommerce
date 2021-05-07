from django.shortcuts import render, get_object_or_404
from .models import Category, Product, ImageAlbum
from cart.forms import AddCartForm


def home(request, slug=None):
    products = Product.objects.filter(inventory__gt=0)
    categories = Category.objects.filter(is_sub=False)
    if slug:
        categories = Category.objects.filter(slug=slug)
    return render(request, 'shop/home.html', {'all_products': products, 'categories': categories})


def product_detail(request, code, year, month, day, slug):
    product = get_object_or_404(Product, slug=slug)
    categories = product.category.all()
    main_category = categories.filter(is_sub=False)
    sub_categories = categories.filter(is_sub=True)
    form = AddCartForm()
    return render(request, 'shop/product_detail.html',
                  {'product': product, 'main_category': main_category, 'sub_categories': sub_categories, 'form': form})
