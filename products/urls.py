
from django.urls import path, include

from .views import ProductListView ,ProductDetailVeiw , CommentCreatView
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [

    path("", ProductListView.as_view(), name = "product_list"),
    path("<int:pk>/", ProductDetailVeiw.as_view(), name = "product_detail"),
    path("comment/<int:pk>" , CommentCreatView.as_view() , name = "comment_create"),






] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
