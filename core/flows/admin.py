from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Project)
class BookAdmin(admin.ModelAdmin):
    prepopulated_fields={'slug':('project_name',),}
    list_display = ['project_name']
    list_filter = ['project_name']
    search_fields = ['project_name']
