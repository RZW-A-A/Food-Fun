from django.contrib import admin
from foodapp.models import Food, Customer, Orderitem, Order, ContactUs, Reservation
# Register your models here.
class Foodadmin(admin.ModelAdmin):
    list_display = ['foodId', 'foodname', 'foodcategory', 'foodprice', 'foodimage', 'fooddiscription']

admin.site.register(Food, Foodadmin)


class Customeradmin(admin.ModelAdmin):
    list_display = ['user', 'name', 'mobile', 'address']

admin.site.register(ContactUs)

admin.site.register(Customer, Customeradmin)
admin.site.register(Order)
admin.site.register(Orderitem)

admin.site.register(Reservation)