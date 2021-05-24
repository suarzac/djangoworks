from django.shortcuts import get_object_or_404, render
from .models import Product

# Create your views here.

def index(request):
    product_list = Product.objects.order_by('product_category')[:5]
    context = {'product_list': product_list}
    return render(request, 'productapp/index.html', context)

def detail(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    return render(request, 'productapp/detail.html', {'product': product})
