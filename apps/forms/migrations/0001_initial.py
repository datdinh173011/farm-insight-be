from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="FormTemplate",
            fields=[
                ("id", models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name="ID")),
                ("template_type", models.CharField(max_length=100, unique=True)),
                ("title", models.CharField(max_length=255)),
                ("description", models.TextField(blank=True)),
                ("source_pdf", models.CharField(blank=True, max_length=255)),
                ("schema", models.JSONField(default=dict)),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
            ],
            options={"ordering": ["title"]},
        ),
        migrations.CreateModel(
            name="FormSubmission",
            fields=[
                ("id", models.BigAutoField(auto_created=True,
                 primary_key=True, serialize=False, verbose_name="ID")),
                ("template_type", models.CharField(max_length=100)),
                ("ho_ten", models.CharField(max_length=255)),
                ("nam_sinh", models.PositiveIntegerField(blank=True, null=True)),
                ("so_dien_thoai", models.CharField(blank=True, max_length=30)),
                ("thon", models.CharField(blank=True, max_length=255)),
                ("xa", models.CharField(blank=True, max_length=255)),
                ("tinh", models.CharField(blank=True, max_length=255)),
                ("data", models.JSONField(default=dict)),
                (
                    "status",
                    models.CharField(
                        choices=[("draft", "Draft"), ("submitted", "Submitted")], default="submitted", max_length=20
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                (
                    "created_by",
                    models.ForeignKey(
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        related_name="form_submissions",
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
                (
                    "template",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, related_name="submissions", to="forms.formtemplate"
                    ),
                ),
            ],
            options={"ordering": ["-created_at"]},
        ),
    ]
