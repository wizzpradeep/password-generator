from django.contrib import admin
from .models import Password

# Register your models here.
class PasswordAdmin(admin.ModelAdmin):
    list_display = ['password']
    ordering = ['created_at']

admin.site.register(Password, PasswordAdmin)