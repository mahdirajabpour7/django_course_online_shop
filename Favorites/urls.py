from django.urls import path
from . import views

urlpatterns = [
    # ...
    path('', views.wishlist, name='wishlist'),  # مسیر لیست علاقه‌مندی‌ها
    path('add/<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),  # مسیر اضافه کردن به لیست علاقه‌مندی‌ها
    path('remove/<int:product_id>/', views.remove_from_wishlist, name='remove_from_wishlist'),  # مسیر حذف از لیست علاقه‌مندی‌ها
    # ...

]
