from django.shortcuts import render
from django.views import generic

from .models import Products

class ProductListView(generic.ListView):
    #model = Products
    queryset = Products.objects.filter(active=True)
    template_name = "Products/Products_list.html"
    context_object_name = "Products"

class ProductDetailVeiw(generic.DetailView):
    model = Products
    template_name = "Products/Products_detail.html"
    context_object_name = "Products"


