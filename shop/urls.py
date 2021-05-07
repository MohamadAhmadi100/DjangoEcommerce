from django.urls import path, re_path
from .views import home, product_detail

app_name = 'shop'
urlpatterns = [
    re_path(r'd/(?P<code>\w+)/(?P<year>\w+)/(?P<month>\w+)/(?P<day>\w+)/(?P<slug>[-\w]+)/', product_detail,
            name='product_detail'),
    re_path(r'd/(?P<slug>[-\w]+)/', home, name='category_filter'),
    path('', home, name='home'),

]
