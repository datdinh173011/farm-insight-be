from django.contrib import admin

from .models import FormSubmission, FormTemplate


@admin.register(FormTemplate)
class FormTemplateAdmin(admin.ModelAdmin):
    list_display = ("title", "template_type", "source_pdf", "updated_at")
    search_fields = ("title", "template_type", "source_pdf")
    readonly_fields = ("created_at", "updated_at")


@admin.register(FormSubmission)
class FormSubmissionAdmin(admin.ModelAdmin):
    list_display = (
        "template",
        "ho_ten",
        "nam_sinh",
        "so_dien_thoai",
        "thon",
        "xa",
        "created_by",
        "status",
        "created_at",
    )
    search_fields = (
        "template__title",
        "template__template_type",
        "created_by__username",
        "ho_ten",
        "nam_sinh",
    )
    list_filter = ("status", "ho_ten", "nam_sinh")
    readonly_fields = ("created_at", "updated_at")
