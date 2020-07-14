from django.shortcuts import render, get_object_or_404
from .models import Product

# Create your views here.
def product_details_view(request, id):
  productset = get_object_or_404(Product, id = id)
  queryset = Product.objects.all()
  context ={
    'object' : queryset,
    'product': productset,
  }
  return render(request, 'Product/base.html', context)