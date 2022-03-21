from rest_framework import serializers
from .models import Product
from rest_framework.validators import UniqueValidator


'''
There are three methods for validators.
1. on model. It is both django and django rest framework. ( Recommanded, use as much as possible)

Sometimes, you will need to do 2 or 3 methods because of validation of title and user unique.
.
2. validate_ in serializer.py
3. add a field in serailier and call external file (validator.py)
'''
def validate_title(value):
    qs = Product.objects.filter(title__exact=value)
    if qs.exists():
        raise serializers.ValidationError(f"{value} is already a product name.")
    return value


def validate_title_no_hello(value):
    if "hello" in value.lower():
        raise serializers.ValidationErrorf(" Hello is not allowed.")
    return value


unique_product_title = UniqueValidator(queryset=Product.objects.all())