from django.contrib import admin
from .models import Project

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "active", "created", "modified")
    prepopulated_fields = {"slug": ("title",)}
