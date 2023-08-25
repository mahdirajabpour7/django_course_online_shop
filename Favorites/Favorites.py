from pyexpat.errors import messages

from products.models import Products
from django.shortcuts import reverse , get_object_or_404
from django.contrib import messages


class Wishlist:
    def __init__(self, request):
        self.request = request
        self.session = request.session
        wishlist = self.session.get("wishlist")
        if wishlist is None:
            self.session["wishlist"] = []
            wishlist = self.session["wishlist"]
        self.wishlist = wishlist

    def add(self, product):
        product_id = str(product.id)
        if product_id not in self.wishlist:
            self.wishlist.append(product_id)
            self.save()

    def remove(self, product):
        product_id = str(product.id)
        if product_id in self.wishlist:
            self.wishlist.remove(product_id)
            self.save()

    def save(self):
        self.session.modified = True

    def __iter__(self):
        product_ids = self.wishlist
        products = Products.objects.filter(id__in=product_ids)
        for product in products:
            yield product

    def __len__(self):
        return len(self.wishlist)

    def clear(self):
        del self.session["wishlist"]
        self.save()

