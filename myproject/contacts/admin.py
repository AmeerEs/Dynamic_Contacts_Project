from django.contrib import admin
from .models import Contact

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ['contact_name', 'email', 'phone', 'created_by', 'created_at', 'updated_by', 'updated_at']
    search_fields = ['contact_name', 'email', 'phone']
    list_filter = ['created_at', 'updated_at']
