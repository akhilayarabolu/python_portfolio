from django.contrib import admin

from .models import Contact, Project


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email", "subject", "is_read", "created_at")
    list_filter = ("is_read", "created_at")
    search_fields = ("name", "email", "subject", "message")
    readonly_fields = ("name", "email", "subject", "message", "created_at")
    list_editable = ("is_read",)
    date_hierarchy = "created_at"


@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ("title", "is_featured", "display_order", "github_url", "live_url")
    list_editable = ("is_featured", "display_order")
    search_fields = ("title", "tech_stack", "description")
