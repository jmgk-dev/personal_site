from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'order', 'archived']
    list_editable = ['order', 'archived']
    list_filter = ['archived']
