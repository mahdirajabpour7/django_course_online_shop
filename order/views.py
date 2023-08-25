from django.shortcuts import render , redirect
from .forms import OrderForm
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from cart.cart import Cart
from .models import OrderItem


@login_required
def order_created_view(request):
    cart = Cart(request)

    order_form=OrderForm()

    if len(cart) == 0:
        messages.warning(request,"your cart is empty")
        return redirect("product_list")


    if request.method == 'POST':
        order_form = OrderForm(request.POST,)

        if order_form.is_valid():
            order_obj = order_form.save(commit=False)
            order_obj.user = request.user
            order_obj.save()

            for item in cart:
                product=item["product_obj"]
                OrderItem.objects.create(product=product, quantity=item["quantity"],order=order_obj,price=product.price,)

            cart.clear()

            request.user.first_name = order_obj.first_name
            request.user.last_name = order_obj.last_name
            request.user.save()


    return render(request,"order/order_detail.html",context={"form":order_form,})
    #return render(request, 'order/order_detail.html', context={
        #"form":OrderForm(),

    #})
