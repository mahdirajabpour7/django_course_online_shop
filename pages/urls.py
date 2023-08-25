from .views import HomePagesView , AboutUsView, UpdatePageView
from django.urls import path

urlpatterns = [

    path ("", HomePagesView.as_view(), name="home"),
    path("aboutus/", AboutUsView.as_view(), name ="about"),
    path ("update/", UpdatePageView.as_view(), name="update"),
]
