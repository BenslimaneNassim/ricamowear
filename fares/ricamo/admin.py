from django.contrib import admin
from .models import *
from django.contrib.auth.models import Group,User
# Register your models here.

admin.site.unregister(User)
admin.site.unregister(Group)
admin.site.register(Design)
admin.site.register(Product)
admin.site.register(Product_images)
admin.site.register(Commande)
admin.site.register(Email)
admin.site.register(Shipping_Price)