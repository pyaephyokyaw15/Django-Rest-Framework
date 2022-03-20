# Actually, this module and codes are in views.py. This is for demostration.

from rest_framework import viewsets, mixins

from .models import Product
from .serializers import ProductSerailizer


class ProductViewSet(viewsets.ModelViewSet):
    """
        get -> list -> Queryset
        get -> retrieve -> Product Instnace Detail View
        post -> create -> New Instance
        put -> Update
        patch -> Partial Update
        delete -> destroy
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'  # default


class ProductGenericViewSet(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    viewsets.GenericViewSet
):
    """
           get -> list -> Queryset
           get -> retrieve -> Product Instnace Detail View
    """

    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'  # default


product_list_view = ProductGenericViewSet.as_view({'get': 'list'})
product_detail_view = ProductGenericViewSet.as_view({'get': 'retrieve'})