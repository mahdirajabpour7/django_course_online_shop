
from django.urls import path, include

from .views import ProductListView ,ProductDetailVeiw

urlpatterns = [

    path("", ProductListView.as_view(), name = "product_list"),
    path("<int:pk>/", ProductDetailVeiw.as_view(), name = "product_detail"),




]
