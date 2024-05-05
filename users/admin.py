from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser, Status

class CustomUserAdmin(UserAdmin):
    model = CustomUser
    list_display = ('phone_number', 'first_name', 'last_name', 'status', 'is_staff', 'is_active',)
    list_filter = ('is_staff', 'is_active',)
    fieldsets = (
        (None, {'fields': ('phone_number', 'password')}),
        ('Personal info', {'fields': ('first_name', 'last_name', 'sms_verify', 'status')}),
        ('Permissions', {'fields': ('is_staff', 'is_active', 'is_superuser')}),
    )
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('phone_number', 'password1', 'password2'),
        }),
    )
    search_fields = ('phone_number', 'first_name', 'last_name',)
    ordering = ('phone_number', 'status')

admin.site.register(CustomUser, CustomUserAdmin)
admin.site.register(Status)