from django.shortcuts import render, get_object_or_404, redirect
from .forms import AddCartForm
from shop.models import Product
from .cart_session import Cart
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required


@login_required
def detail(request):
    cart = Cart(request)
    return render(request, 'cart/detail.html', {'cart': cart})


@login_required
def add_cart(request, product_id):
    if request.method == 'POST':
        cart = Cart(request)
        product = get_object_or_404(Product, id=product_id)
        form = AddCartForm(request.POST)
        if form.is_valid():
            cart.add(product=product, quantity=form.cleaned_data['quantity'])
    return redirect('cart:detail')


def remove_cart(request, product_id):
    cart = Cart(request)
    product = get_object_or_404(Product, id=product_id)
    cart.remove(product)
    return redirect('cart:detail')
