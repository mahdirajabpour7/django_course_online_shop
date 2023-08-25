from django.db import models
from django.conf import settings
#from django.utils.translation import gettext as_



class Order(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)

    phone_number = models.CharField(max_length=13)

    address = models.CharField(max_length=500)

    is_paid = models.BooleanField(default=False)
    order_notes = models.TextField()

    datetime = models.DateTimeField(auto_now_add=True)
    atetime_modified = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Order: {self.id}"


class OrderItem(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='items')

    product = models.ForeignKey("products.Products", on_delete=models.CASCADE , related_name="order_items")
    quantity = models.PositiveIntegerField(default=1)
    price = models.PositiveIntegerField()

    def __str__(self):
        return f"OrderItem {self.id} : {self.product}*{self.quantity} (price:{self.price})"




