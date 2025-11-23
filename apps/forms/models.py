from django.conf import settings
from django.db import models


class FormTemplate(models.Model):
    template_type = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=255)
    description = models.TextField(blank=True)
    source_pdf = models.CharField(max_length=255, blank=True)
    schema = models.JSONField(default=dict)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class FormSubmission(models.Model):
    STATUS_CHOICES = (
        ("draft", "Draft"),
        ("submitted", "Submitted"),
    )

    template = models.ForeignKey(
        FormTemplate, on_delete=models.CASCADE, related_name="submissions")
    template_type = models.CharField(max_length=100)
    ho_ten = models.CharField(max_length=255)
    nam_sinh = models.DateField(null=True, blank=True)
    so_dien_thoai = models.CharField(max_length=30, blank=True)
    thon = models.CharField(max_length=255, blank=True)
    xa = models.CharField(max_length=255, blank=True)
    tinh = models.CharField(max_length=255, blank=True)
    data = models.JSONField(default=dict)
    status = models.CharField(
        max_length=20, choices=STATUS_CHOICES, default="submitted")
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True, related_name="form_submissions"
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        ordering = ["-created_at"]

    def __str__(self):
        return f"{self.template.template_type} - {self.created_at:%Y-%m-%d}"
