from django.urls import path
from .views import detail, add_cart, remove_cart

app_name = 'cart'
urlpatterns = [
    path('', detail, name='detail'),
    path('add/<int:product_id>/', add_cart, name='add_cart'),
    path('remove/<int:product_id>/', remove_cart, name='remove_cart'),
]
