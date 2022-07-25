"""Register your models here"""
from django.contrib import admin
from .models import ComponentType,Manufacturer,Product,ProductCategory,Specifications,User,Component

class UserAdmin(admin.ModelAdmin):
    """User model register"""
admin.site.register(User, UserAdmin)

class ProductCategoryAdmin(admin.ModelAdmin):
    """Category model register"""
admin.site.register(ProductCategory, ProductCategoryAdmin)

class ManufacturerAdmin(admin.ModelAdmin):
    """Manufacturer model register"""
admin.site.register(Manufacturer, ManufacturerAdmin)

class ComponentTypeAdmin(admin.ModelAdmin):
    """Component type model register"""
admin.site.register(ComponentType, ComponentTypeAdmin)

class ComponentAdmin(admin.ModelAdmin):
    """Component model register"""
admin.site.register(Component, ComponentAdmin)

class ProductAdmin(admin.ModelAdmin):
    """Product model register"""
admin.site.register(Product, ProductAdmin)

class SpecificationsAdmin(admin.ModelAdmin):
    """Specs model register"""
admin.site.register(Specifications,SpecificationsAdmin)
