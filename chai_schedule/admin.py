
# Register your models here.
from django.contrib import admin

from .models import Employee

@admin.register(Employee)
class PostAdmin(admin.ModelAdmin):

    # set columns to be displayed
    list_display = ['first_name', 'last_name']

    # set column filters
    list_filter = ['first_name', 'last_name']

    # # set search fields
    search_fields = ['first_name', 'last_name']

    # order columns by status and publish by default
    ordering = ['last_name', 'first_name']
