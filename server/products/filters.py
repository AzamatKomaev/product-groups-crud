from django_filters import FilterSet
from .models import ProductGroup, Product


class ProductGroupFilter(FilterSet):
    class Meta:
        model = ProductGroup
        fields = ['category_id']


class ProductFilter(FilterSet):
    class Meta:
        model = Product
        fields = ['group_id']

