from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from .models import Product, ProductGroup, ProductCategory
from .serializers import ProductSerializer, ProductGroupSerializer, ProductCategorySerializer
from .paginations import DefaultPagination


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = DefaultPagination


class ProductGroupViewSet(ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    pagination_class = DefaultPagination


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
