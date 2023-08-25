from django.contrib import admin


from dotenv.main import with_warn_for_invalid_lines

from .models import Order , OrderItem

from jalali_date.admin import ModelAdminJalaliMixin



class OrderInline(ModelAdminJalaliMixin,admin.TabularInline):
    model = OrderItem
    fialds = ["order" , "product" , "quantity" , "price" ,]





@admin.register(Order)
class OrderAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ["user", "first_name", "last_name", "is_paid",]
    inlines = [
        OrderInline,
    ]

@admin.register(OrderItem)
class OrderItemAdmin(ModelAdminJalaliMixin,admin.ModelAdmin):
    list_display = ["order", "product", "quantity",]

