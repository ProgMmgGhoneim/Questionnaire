from django.contrib import admin

from .models.merchant import Merchant

@admin.register(Merchant)
class MerchnatAdmin(admin.ModelAdmin):
    list_display = ('id', 'user', 'is_live', 'created_at', 'updated_at')