from django.db import models
from django.shortcuts import reverse
from django.contrib.auth import get_user_model
from django.utils.translation import gettext_lazy as _
from django.utils import timezone
from django.conf import settings


from django_ckeditor_5.fields import CKEditor5Field
from ckeditor.fields import RichTextField



class Products(models.Model):
    title = models.CharField(max_length=100)
    description = RichTextField()


    datetime = models.DateTimeField(auto_now_add=True)

    price = models.PositiveIntegerField(default=0)
    active = models.BooleanField(default=True)
    datetime_modified = models.DateTimeField(default=timezone.now)
    status = models.BooleanField(default=False)

    short_description=models.TextField(blank=True)

    image = models.ImageField(verbose_name=_('Product_Image'), upload_to="product/product_cover/" , blank=True)
    pdf_file = models.FileField(verbose_name=_('Product_PDF'), upload_to="product/pdfs", blank=True, null=True)

    def get_likes(self):
        return self.like_set.filter(value=True).count()

    def get_dislikes(self):
        return self.like_set.filter(value=False).count()

    def is_liked_by(self, user):
        return self.like_set.filter(user=user, value=True).exists()

    def is_disliked_by(self, user):
        return self.like_set.filter(user=user, value=False).exists()

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



class Like(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    product = models.ForeignKey(Products, on_delete=models.CASCADE)
    value = models.BooleanField() # True for like, False for dislike
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} {'likes' if self.value else 'dislikes'} {self.product}"


