from django.db.models.deletion import ProtectedError
from rest_framework.viewsets import ModelViewSet
from rest_framework.generics import ListCreateAPIView
from rest_framework.exceptions import APIException
from .models import Product, ProductGroup, ProductCategory
from .serializers import ProductSerializer, ProductGroupSerializer, ProductCategorySerializer
from .paginations import DefaultPagination
from .filters import ProductGroupFilter, ProductFilter


class ProtectedInstanceError(APIException):
    status_code = 400
    default_detail = 'You cannot delete the instance as it has related data.'


class ProductCategoryViewSet(ModelViewSet):
    queryset = ProductCategory.objects.all()
    serializer_class = ProductCategorySerializer
    pagination_class = DefaultPagination

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError:
            raise ProtectedInstanceError


class ProductGroupViewSet(ModelViewSet):
    queryset = ProductGroup.objects.all()
    serializer_class = ProductGroupSerializer
    pagination_class = DefaultPagination
    filterset_class = ProductGroupFilter

    def perform_destroy(self, instance):
        try:
            instance.delete()
        except ProtectedError:
            raise ProtectedInstanceError


class ProductAPIView(ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    pagination_class = DefaultPagination
    filterset_class = ProductFilter
