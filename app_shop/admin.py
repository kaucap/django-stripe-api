from django.contrib import admin
from app_shop.models import Item


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):
    list_display = ['name', 'description', 'price', 'currency']
