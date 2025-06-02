from django.contrib import admin
from .models import Car, Brand, Model, VehicleType, CarImage, Color

class CarImageInline(admin.TabularInline):
    model = CarImage
    extra = 1

@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    inlines = [CarImageInline]
    list_display = ('id', 'brand', 'model', 'vehicle_type', 'owner', 'year', 'dealer')
    search_fields = ('brand__name', 'model__name',)
    list_filter = ('brand', 'vehicle_type', 'dealer')
    
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')

@admin.register(Model)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'brand', 'start_year', 'end_year')

@admin.register(VehicleType)
class VehicleTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')
   
@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ('id', 'car', 'image')

@admin.register(Color)
class ColorAdmin(admin.ModelAdmin):
    list_display = ['id', 'name']