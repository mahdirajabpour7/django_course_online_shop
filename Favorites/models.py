from django.db import models
from django.conf import settings



class WishlistItem(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)

    product = models.ForeignKey("products.Products", on_delete=models.CASCADE)  # مدل محصولات شما
    added_date = models.DateTimeField(auto_now_add=True)

