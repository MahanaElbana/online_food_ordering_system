from django.contrib import admin
from .models import Menu ,Category ,Customer ,Restaurant ,Reating ,Reservation ,Order
# Register your models here.
admin.site.register(Menu)
admin.site.register(Restaurant)
admin.site.register(Category)
admin.site.register(Customer)
admin.site.register(Order)
admin.site.register(Reservation)
admin.site.register(Reating)