from django.contrib import admin
from .models import *

# Register your models here.

admin.site.register(Customer)
admin.site.register(Product)
admin.site.register(Order)
admin.site.register(OrderItem)
admin.site.register(ShippingAddress)

##### CLOTHINGS ######

admin.site.register(Bags)
admin.site.register(Blouses)
admin.site.register(Gele)
admin.site.register(Gowns)
admin.site.register(Shoes)
admin.site.register(Tops)

##### OTHERS ######

admin.site.register(Jewelries)
admin.site.register(Makeups)
admin.site.register(Purses)
admin.site.register(Wigs)
admin.site.register(Sunglasses)
