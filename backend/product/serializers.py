from  rest_framework import serializers
from .models import Product

class ProductSerailizer(serializers.ModelSerializer):
    # if we want different name to model field
    my_discount = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'pk',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # except this method (get_<field_name>)
    def get_my_discount(self, obj):
        return obj.discount()



