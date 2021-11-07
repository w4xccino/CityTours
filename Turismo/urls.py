from django.urls import path
from .views import index, lugares

urlpatterns = [
    path("index/",index, name="index"),
    path("lugares/", lugares ,name="lugares"),
]
