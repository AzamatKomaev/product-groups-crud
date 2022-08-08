from django.urls import path
from . import views


urlpatterns = [
    path('product-categories/', views.ProductCategoryViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product-categoires/<int:pk>/', views.ProductCategoryViewSet.as_view({'get': 'retrieve'})),
    path('product-groups', views.ProductGroupViewSet.as_view({'get': 'list', 'post': 'create'})),
    path('product-groups/<int:pk>/', views.ProductGroupViewSet.as_view({'get': 'retrieve'})),
    path('products/', views.ProductAPIView.as_view())
]
