from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .Favorites import Wishlist
from products.models import Products



from .models import  WishlistItem # اگر کلاس Wishlist در همان فایل موجود نیست، مسیر دقیق را وارد کنید

def wishlist(request):
    wishlist = Wishlist(request)
    products = wishlist.__iter__()  # محصولات لیست علاقه‌مندی‌ها
    context = {'products': products}
    return render(request, 'Favorites/Favorites.html', context)

def add_to_wishlist(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    wishlist = Wishlist(request)
    wishlist.add(product)
    return redirect('wishlist')

def remove_from_wishlist(request, product_id):
    product = get_object_or_404(Products, id=product_id)
    wishlist = Wishlist(request)
    wishlist.remove(product)
    return redirect('wishlist')




