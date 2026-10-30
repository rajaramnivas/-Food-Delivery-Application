from django.contrib import admin

from .models import Profile,Restaurant,FoodItem,Order

admin.site.register(Profile)
admin.site.register(Restaurant)
admin.site.register(FoodItem)
admin.site.register(Order)
