from django.contrib import admin

from .models import FormSubmission, FormTemplate


@admin.register(FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ("title", "slug", "source_pdf", "updated_at")
    search_fields = ("title", "slug", "source_pdf")
    readonly_fields = ("created_at", "updated_at")


@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = ("template", "created_by", "status", "created_at")
    search_fields = ("template__title", "template__slug", "created_by__username")
    list_filter = ("status",)
    readonly_fields = ("created_at", "updated_at")
