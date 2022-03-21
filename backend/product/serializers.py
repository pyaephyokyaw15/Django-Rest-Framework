from  rest_framework import serializers
from rest_framework.reverse import reverse
from .models import Product
from .validators import validate_title, validate_title_no_hello, unique_product_title

class ProductSerailizer(serializers.ModelSerializer):
    # if we want different name to model field
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    my_url = serializers.HyperlinkedIdentityField(view_name='product-detail',
                                                  lookup_field='pk')
    email = serializers.EmailField(write_only=True)
    title = serializers.CharField(validators=[validate_title, validate_title_no_hello, unique_product_title])
    name = serializers.CharField(source='title', read_only=True)

    class Meta:
        model = Product
        fields = [
            'my_url',
            'url',
            'pk',
            'name'
            'email',
            'title',
            'content',
            'price',
            'sale_price',
            'my_discount'
        ]

    # def validate_title(self, value):
    #     request = self.context.get('request')
    #     user = request.user
    #     qs = Product.objects.filter(user=user, title__exact=value)
    #     if qs.exists():
    #         raise serializers.ValidationError(f"{value} is already a product name.")
    #     return value



    def create(self, validated_data):
        # return Product.objects.create(**validated_data)
        print(validated_data)
        email = validated_data.pop('email')
        obj = super().create(validated_data)
        #
        print(email, obj)
        print(validated_data)
        return obj

    def update(self, instance, validated_data):
        email = validated_data.pop('email')
        return super().update(instance, validated_data)


    # except this method (get_<field_name>)
    def get_my_discount(self, obj):
        return obj.discount()

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}"
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)


class ProductDetailSerailizer(serializers.ModelSerializer):
    # if we want different name to model field
    my_discount = serializers.SerializerMethodField(read_only=True)
    url = serializers.SerializerMethodField(read_only=True)
    my_url = serializers.HyperlinkedIdentityField(view_name='product-detail',
                                                  lookup_field='pk')
    edit_url = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Product
        fields = [
            'my_url',
            'url',
            'edit_url',
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

    def get_url(self, obj):
        # return f"/api/products/{obj.pk}"
        print(self.r)
        request = self.context.get('request') # self.request
        if request is None:
            return None
        return reverse("product-detail", kwargs={"pk": obj.pk}, request=request)

    def get_edit_url(self, obj):
        request = self.context.get('request')  # self.request
        if request is None:
            return None
        return reverse("product-edit", kwargs={"pk": obj.pk}, request=request)


