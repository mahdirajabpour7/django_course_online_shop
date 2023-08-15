from django.contrib import admin
from django.urls import path, include
from .views import order_created_view



urlpatterns = [
    path("create/" , order_created_view , name="order_create"),



]