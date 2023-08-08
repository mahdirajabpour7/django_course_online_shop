from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone


class Products(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    datetime = models.DateTimeField(auto_now_add=True)

    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_modified = models.DateTimeField(default=timezone.now)

    image = models.ImageField(verbose_name=_('Product_Image'), upload_to="product/product_cover" , blank=True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse("product_detail", args=[self.pk])


class ActiveCommentsManager(models.Manager):
    def get_queryset(self):
        return super(ActiveCommentsManager, self).get_queryset().filter(active=True)




class Comment(models.Model):
    PRODUCT_START = [
        ("1", "very_bad"),
        ("2", "bad"),
        ("3", "NORMAL"),
        ("4", "GOOD"),
        ("5", "VERY GOOD"),
    ]

    product = models.ForeignKey(Products, on_delete=models.CASCADE, related_name="comments", )
    body = models.TextField()
    author = models.ForeignKey(get_user_model(), on_delete=models.CASCADE, related_name="comments", )
    stars = models.CharField(max_length=10, choices=PRODUCT_START)
    #datetime_modified = models.DateTimeField(auto_now=True)

    datetime_modified = models.DateTimeField(default=timezone.now)


    datetime = models.DateTimeField(auto_now_add=True)
    active = models.BooleanField(default=True)




    object = models.Manager()
    active_comments_manager = ActiveCommentsManager(    )




    def get_absolute_url(self):
        return reverse("product_detail", args=[self.product.id])

