from django.shortcuts import render

# Create your views here.
def home_view(request):
  context={}
  return render(request, 'base.html', context)

def product_view(request):
  context={}
  return render(request, 'base.html', context)


def about_view(request):
  context={}
  return render(request, 'base.html', context)


def contact_view(request):
  context={}
  return render(request, 'base.html', context)
