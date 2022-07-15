from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("product/<str:product_name>/",views.product,name="product"),
    path("product/<str:product_name>/checkout/",views.checkout,name="checkout"),
    path("brand/",views.brand,name="brand"),
    path("category/<str:category_name>/",views.category,name="category"),
    path("category/<str:category_name>/<str:categories_name>/",views.categories,name="category"),
    path("designs/",views.design,name="design"),
    path("search/<str:searched>/",views.search,name="search"),
]