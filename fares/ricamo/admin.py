from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Color)
admin.site.register(Product)
admin.site.register(Product_images)
admin.site.register(Commande)
admin.site.register(Email)
admin.site.register(Shipping_Price)
admin.site.register(Category)
admin.site.register(To_order)