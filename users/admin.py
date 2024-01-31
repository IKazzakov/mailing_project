from django.contrib import admin

from users.models import User


# Register your models here.


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'is_active', 'is_staff')
    search_fields = ('first_name', 'last_name', 'email')
    list_filter = ('is_active', 'is_staff')