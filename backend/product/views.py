from django.shortcuts import render

# Create your views here.
from rest_framework import authentication, generics, mixins, permissions
from .models import Product
from .permissions import IsStaffEditorPermission
from .serializers import ProductSerailizer
from rest_framework.decorators import api_view
from rest_framework.response import Response
from django.shortcuts import render, get_object_or_404


class ProductCreateAPIVIew(generics.CreateAPIView):
    # api/products/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print(serializer)
        serializer.save()


class ProductDetailAPIView(generics.RetrieveAPIView):
    # api/products/<int:pk>/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    # lookup_field = 'pk'



class ProductUpdateAPIView(generics.UpdateAPIView):
    # api/products/<int:pk>/update/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'

    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content = instance.title
            instance.save()


class ProductDeleteAPIView(generics.DestroyAPIView):
    # api/products/<int:pk>/delete/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    lookup_field = 'pk'
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes = [permissions.DjangoModelPermissions]

    def perform_destroy(self, instance):
        # instance
        super().perform_destroy(instance)


class ProductListAPIView(generics.ListAPIView):
    # api/products/list/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer


class ProductListCreateAPIVIew(generics.ListCreateAPIView):
    # api/products/list/create/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer
    authentication_classes = [authentication.SessionAuthentication]
    # permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    #permission_classes = [permissions.DjangoModelPermissions]
    permission_classes = [IsStaffEditorPermission]

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print('Validated Data', serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        print(serializer)
        # print('Data', serializer.data)
        serializer.save(content=content)
        print('Data', serializer.data)


class ProductMixinView(
    mixins.CreateModelMixin,
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
):
    # api/products/list/
    queryset = Product.objects.all()
    serializer_class = ProductSerailizer

    def get(self, request, *args, **kwargs):
        print(args, kwargs)
        pk = kwargs.get("pk")
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)

    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)

    def perform_create(self, serializer):
        # serializer.save(user=self.request.user)
        print('Validated Data', serializer.validated_data)
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = "This is a single view doing cool stuff."
        print(serializer)
        # print('Data', serializer.data)
        serializer.save(content=content)
        print('Data', serializer.data)





@api_view(['GET', 'POST'])
def product_alt_view(request, pk=None, *args, **kwargs):

    # we can also write
    # def product_alt_view(request, *args, **kwargs):
    # if so
    # kwargs = {'pk':10}


    method = request.method

    print(args)
    print(kwargs)
    if method == "GET":

        if pk is not None:
            # api/products/<int:pk>/
            # detail view
            obj = get_object_or_404(Product, pk=pk)
            data = ProductSerailizer(obj, many=False).data
            return Response(data)
        else:
            # api/products/
            # list view
            queryset = Product.objects.all()
            data = ProductSerailizer(queryset, many=True).data
            return Response(data)

    if method == "POST":
        serializer = ProductSerailizer(data=request.data)
        if serializer.is_valid(raise_exception=True):
            title = serializer.validated_data.get('title')
            content = serializer.validated_data.get('content') or None
            if content is None:
                content = title
            serializer.save(content=content)
            return Response(serializer.data)
