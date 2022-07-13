from django.contrib import admin

# Register your models here.

from django.contrib import admin
from .models import User

class UserAdmin(admin.ModelAdmin):
    pass
admin.site.register(User, UserAdmin)
