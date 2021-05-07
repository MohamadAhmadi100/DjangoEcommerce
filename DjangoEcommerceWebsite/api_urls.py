from rest_framework import routers
from shop.api_views import ProductViewSet, CategoryViewSet
from accounts.api_views import UserViewSet

router = routers.DefaultRouter()
router.register('product', ProductViewSet, basename='product')
router.register('category', CategoryViewSet, basename='category')
router.register('user', UserViewSet, basename='user')
urlpatterns = router.urls
