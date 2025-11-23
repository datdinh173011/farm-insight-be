from django.core.management.base import BaseCommand

from apps.forms.data.pdf_form_schemas import FORM_SCHEMAS
from apps.forms.models import FormTemplate


class Command(BaseCommand):
    help = "Seed form templates derived from the PDF questionnaires."

    def handle(self, *args, **options):
        for template in FORM_SCHEMAS:
            obj, created = FormTemplate.objects.update_or_create(
                slug=template["slug"],
                defaults={
                    "title": template["title"],
                    "description": template.get("description", ""),
                    "source_pdf": template.get("source_pdf", ""),
                    "schema": template["schema"],
                },
            )
            action = "Created" if created else "Updated"
            self.stdout.write(self.style.SUCCESS(f"{action} template {obj.slug}"))
