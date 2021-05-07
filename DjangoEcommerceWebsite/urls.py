from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from rest_framework.authtoken.views import obtain_auth_token
from .api_urls import router

urlpatterns = [
                  path('admin/', admin.site.urls),
                  path('accounts/', include('accounts.urls', namespace='accounts')),
                  path('cart/', include('cart.urls', namespace='cart')),
                  path('orders/', include('orders.urls', namespace='orders')),
                  path('', include('shop.urls', namespace='shop')),
                  path('api-auth/', include('rest_framework.urls')),
                  # path('api/', include('restapi.urls', namespace='api')),
                  path('api-token-auth/', obtain_auth_token),
                  path('api/', include(router.urls)),
              ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
