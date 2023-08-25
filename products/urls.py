
from django.urls import path, include

from .views import ProductListView ,ProductDetailVeiw , CommentCreatView ,search_products, like_product, dislike_product,download_pdf,ProductsCreateView
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [

    path("", ProductListView.as_view(), name = "product_list"),
    path("<int:pk>/", ProductDetailVeiw.as_view(), name = "product_detail"),
    path("comment/<int:pk>" , CommentCreatView.as_view() , name = "comment_create"),
    path('search/', search_products, name='search_products'),
    path('products/<int:pk>/like/', like_product, name='like-product'),
    path('products/<int:pk>/dislike/', dislike_product, name='dislike-product'),
    path('download_pdf/', download_pdf, name='download_pdf'),
    #url('download_my_pdf', download_pdf),
    path("create/",ProductsCreateView.as_view(), name='create'),


] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
