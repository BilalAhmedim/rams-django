from django.shortcuts import render, get_object_or_404
from .models import Product, Category

# Create your views here.
def product_details_view(request, id):
  productset = get_object_or_404(Product, id = id)
  queryset = Product.objects.all()
  context ={
    'object' : queryset,
    'product': productset,
  }
  return render(request, 'Product/base.html', context)

def product_category_view(request):
  categoryset = Category.objects.all()
  context ={
    'category': categoryset,
  }
  return render(request, 'Product/base.html', context)

def absolute_product_view(request, product):
  absoluteproduct = Product.objects.filter(category__name=product)
  context ={
    'absolutecategory': absoluteproduct,
  }
  return render(request, 'Product/base.html', context)