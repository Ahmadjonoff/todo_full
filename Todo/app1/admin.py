from django.contrib import admin
from django.contrib.admin import ModelAdmin

from .models import *

@admin.register(TODO)
class TODOadmin(ModelAdmin):
    search_fields = ['title']
    list_filter = ['status']