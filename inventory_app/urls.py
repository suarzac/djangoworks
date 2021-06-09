from django.urls import re_path
from django.views.generic import ListView, UpdateView, DetailView
from .views import ProductList, ProductDetail, CreateProduct, DeleteProduct, UpdateProduct
from .models import Product, Category

app_name = 'products'

urlpatterns = [
    # List all products ex.: /products/
    re_path(r'^$', ProductList.as_view(), name='product_list'),

    # Provide details for product, ex.: /products/1/
    re_path(r'^(?P<pk>\d+)/$', ProductDetail.as_view(), name='product_detail'),

    # Delete product, ex.: /products/delete/1/
    re_path(r'^delete/(?P<pk>\d+)$', DeleteProduct.as_view(), name='product_delete'),

    # Create a new product ex.: /products/create
    re_path(r'^create/$', CreateProduct.as_view(), name='product_create'),
    
    # Update a current product ex.: /products/update/1
    re_path(r'^update/(?P<pk>\d+)$', UpdateProduct.as_view(), name='product_update'), 
    
]