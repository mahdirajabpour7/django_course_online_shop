from django.shortcuts import render, get_object_or_404, redirect
from .cart import Cart
from products.models import Products
from .forms import AddToCart
from django.contrib import messages

def cart_detail_view(request):
    #return render(request, "cart/cart_detail.html",)
    cart = Cart(request)
    print(len(cart))
    for item in cart:
        item["product_update_quantity_form"] = AddToCart(initial={
            "quantity": item["quantity"],
            "inplace": True,
        })

    return render(request, "cart/cart_detail.html",{
        "cart":cart,
        })
def add_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)  # تغییر نام متغیر از product به product_id

    form = AddToCart(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = int(cleaned_data["quantity"])
        cart.add(product, quantity, replace=cleaned_data["inplase"])

    return redirect("cart_detail_view")


def aadd_to_cart_view(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)

    form = AddToCart(request.POST)

    if form.is_valid():
        cleaned_data = form.cleaned_data
        quantity = int(cleaned_data["quantity"])
        Cart.add(product,quantity)


    return redirect("cart_detail")

def remove_from_cart(request, product_id):
    cart = Cart(request)

    product = get_object_or_404(Products, id=product_id)  # تغییر نام متغیر از product به product_id

    cart.remove(product)

    messages.success(request, "removed product")

    return redirect("cart_detail_view")





