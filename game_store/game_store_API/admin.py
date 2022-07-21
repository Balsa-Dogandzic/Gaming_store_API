from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import ComponentType, Manufacturer, Product, ProductCategory, Specifications, User, Component

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)


class ProductCategoryAdmin(admin.ModelAdmin):
    pass
admin.site.register(ProductCategory, ProductCategoryAdmin)


class ManufacturerAdmin(admin.ModelAdmin):
    pass
admin.site.register(Manufacturer, ManufacturerAdmin)


class ComponentTypeAdmin(admin.ModelAdmin):
    pass
admin.site.register(ComponentType, ComponentTypeAdmin)


class ComponentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Component, ComponentAdmin)


class ProductAdmin(admin.ModelAdmin):
    pass
admin.site.register(Product, ProductAdmin)


class SpecificationsAdmin(admin.ModelAdmin):
    pass
admin.site.register(Specifications,SpecificationsAdmin)