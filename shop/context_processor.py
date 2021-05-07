from .models import Category, Product


def all_data(request):
    nav_products = Product.objects.all()
    nav_categories = Category.objects.all()
    return {'nav_products': nav_products, 'nav_categories': nav_categories}
