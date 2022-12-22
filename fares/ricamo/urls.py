from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index,name='index'),
    path("product/<str:product_name>/",views.product,name="product"),
    path("checkout/",views.checkout,name="checkout"),
    #path("checkout/",views.checkout_cart,name="checkout"),
    path("search/",views.search,name="search"),
    path("email/",views.mail_handle,name="email"),
    path("brand/",views.brand,name="brand"),
    path("category/<str:category_name>/",views.category,name="category"),
    #path("category/<str:category_name>/<str:categories_name>/",views.categories,name="category"),
    #path("designs/",views.design,name="design"),
]