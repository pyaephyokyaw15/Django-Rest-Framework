# Actually, this module and codes are in urls.py. This is for demostration.
from rest_framework.routers import DefaultRouter
from product.viewsets import ProductViewSet, ProductGenericViewSet
router = DefaultRouter()
router.register('products-abc', ProductViewSet, basename='products')

urlpatterns = router.urls
print(urlpatterns)
