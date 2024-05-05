from django.contrib import admin
from .models import Seller


class SellerAdmin(admin.ModelAdmin):
    list_display = ('phone_number', "first_name", "last_name", 'owner')
    search_fields = ('phone_number', "first_name", "last_name", "owner")

    def display_profile_image(self, obj):
        return obj.profile_image.url if obj.profile_image else 'No Image'

    display_profile_image.short_description = 'Profile Image'


admin.site.register(Seller, SellerAdmin)