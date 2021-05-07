from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from .models import Order, OrderItem
from shop.models import Product
from cart.cart_session import Cart
from zeep import Client
from django.http import HttpResponse


@login_required
def create_order(request):
    cart = Cart(request)
    if cart.cart:
        try:
            order = Order.objects.create(user=request.user)
        except:
            order = Order.objects.get(user=request.user)
        for item in cart:
            product = get_object_or_404(Product, id=int(item['product'].id))
            OrderItem.objects.create(order=order, product=product, price=product.price,
                                     quantity=item['quantity'])
        cart.clear()
        return redirect('orders:request')
    else:
        return redirect('shop:home')


@login_required
def order_detail(request, order_id):
    order = get_object_or_404(Order, id=order_id)
    return render(request, 'orders/order_detail.html', {'order': order})


MERCHANT = '11111111-2222-3333-4444-55555555555'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = "پرداخت از فروشگاه جنگو"
CallbackURL = 'http://localhost:8000/orders/verify/'


@login_required
def send_request(request):
    order = get_object_or_404(Order, user=request.user)
    amount = order.get_total_cost()
    result = client.service.PaymentRequest(MERCHANT, amount, description, CallbackURL=CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        return render(request, 'orders/order_error.html')


@login_required
def verify(request):
    order = get_object_or_404(Order, user=request.user)
    amount = order.get_total_cost()
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            order.paid = True
            order.save()
            return render(request, 'orders/order_success.html', {'ref_id': str(result.RefID)})
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return render(request, 'orders/order_error.html')
    else:
        return render(request, 'orders/order_error.html')
