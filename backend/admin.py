from django.contrib import admin
from backend.models import *


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'quantity_in_stock')
    ordering = ('price', 'quantity_in_stock')


@admin.register(Establishment)
class EstablishmentAdmin(admin.ModelAdmin):
    list_display = ('name', 'opening_hour', 'closing_hour', 'location')
    ordering = ('opening_hour', 'closing_hour')
