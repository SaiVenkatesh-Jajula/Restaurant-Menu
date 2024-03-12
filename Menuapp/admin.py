from django.contrib import admin
from .models import Menu


# Register your models here.
class CustomizeInterface(admin.ModelAdmin):
    list_display = ("menu_item", "dish_name", "price")
    list_filter = ("status",)
    search_fields = ("dish_name", "menu_item")


admin.site.register(Menu, CustomizeInterface)