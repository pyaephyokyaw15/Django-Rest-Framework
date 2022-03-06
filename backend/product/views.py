from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Product
from .serializers import ProductSerailizer


class ProductCreateAPIVIew(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer)
        serializer.save()
    

class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    # lookup_field = 'pk'


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    # lookup_field = 'pk'


class ProductListCreateAPIVIew(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        print(serializer)
        serializer.save(content=content)
        print(serializer.data)