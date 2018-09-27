from django.shortcuts import render
from django.template import loader
from django.http import HttpResponse
from .models import Product

def index(request):
    all_products=Product.objects.all()
    context = {
        'all_products' : all_products,
    }
    return render(request, 'products/index.html',context)

def detail(request,product_id):
    return HttpResponse("Id of this product is "+str(product_id))