from django.contrib import admin

from .models import *

# Register your models here.

admin.site.register(RestaurantChain)
admin.site.register(Restaurant)
admin.site.register(Menu)
admin.site.register(Dish)
admin.site.register(DishType)
admin.site.register(Ingredient)
admin.site.register(PhoneNumber)
