from django.urls import path
from .views import create_order, order_detail, send_request, verify

app_name = 'orders'
urlpatterns = [
    path('create/', create_order, name='create'),
    path('detail/<int:order_id>/', order_detail, name='detail'),
    path('request/', send_request, name='request'),
    path('verify/', verify, name='verify'),
]
