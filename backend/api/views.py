# Create your views here.
from rest_framework.response import Response

from rest_framework.decorators import api_view
from product.models import Product
from product.serializers import ProductSerailizer
from rest_framework import status


@api_view(["POST"])
def api_home(request):
    serializer = ProductSerailizer(data=request.data)
    # print(serializer.data)
    if serializer.is_valid(raise_exception=True):
        print('Serializer', serializer)
        print('Type of Serializer', type(serializer))

        instance = serializer.save()
        data = serializer.data
        print('Data', data)
        print('Type of Serializer', type(data))
        return Response(data)

    # return Response({"invalid":"not good data"}, status=status.HTTP_400_BAD_REQUEST)

