from django.shortcuts import render
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin
from django.views.generic import ListView, DetailView, CreateView, DeleteView, UpdateView
from .models import Product

# Create your views here.

class ProductList(LoginRequiredMixin, ListView):
    model = Product
    template_name = 'inventory_app/product_list.html'
    context_object_name = 'product_list'

class ProductDetail(DetailView):
    model = Product
    template_name = 'inventory_app/product_detail.html'
    context = ''

''' TODO fix permission_required attr '''
class CreateProduct(PermissionRequiredMixin, CreateView):
    permission_required = ''
    model = Product
    fields = ['product_name', 'product_category', 'product_description', 'product_price', 'product_image']
    template_name = 'inventory_app/product_create.html' 
    success_url = reverse_lazy('products:product_list')

class DeleteProduct(DeleteView):
    model = Product
    template_name = 'inventory_app/product_delete.html'
    success_url = reverse_lazy('products:product_list')

class UpdateProduct(UpdateView):
    model = Product
    fields = ['product_name', 'product_category', 'product_description', 'product_price', 'product_image']
    template_name = 'inventory_app/product_update.html' 
    success_url = reverse_lazy('products:product_list') 

