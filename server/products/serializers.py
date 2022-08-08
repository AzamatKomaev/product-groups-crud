from rest_framework.serializers import ModelSerializer
from .models import ProductCategory, ProductGroup, Product


class ProductCategorySerializer(ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


class ProductGroupSerializer(ModelSerializer):
    class Meta:
        model = ProductGroup
        fields = '__all__'


class ProductSerializer(ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'
