from typing import Iterable, Set

from rest_framework import serializers

from .models import FormSubmission, FormTemplate


class FormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = ("id", "slug", "title", "description", "source_pdf", "schema", "created_at", "updated_at")
        read_only_fields = fields


def _collect_required_keys(schema: dict) -> Set[str]:
    required: Set[str] = set()

    def visit(field: dict):
        if field.get("required"):
            key = field.get("key")
            if key:
                required.add(key)
        nested_fields: Iterable[dict] = field.get("fields", []) or field.get("columns", [])
        for nested in nested_fields:
            visit(nested)

    for section in schema.get("sections", []):
        for field in section.get("fields", []):
            visit(field)
    return required


class FormSubmissionSerializer(serializers.ModelSerializer):
    template = serializers.SlugRelatedField(slug_field="slug", queryset=FormTemplate.objects.all())

    class Meta:
        model = FormSubmission
        fields = (
            "id",
            "template",
            "data",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at")

    def validate(self, attrs):
        template: FormTemplate = attrs["template"]
        data = attrs.get("data") or {}
        required_keys = _collect_required_keys(template.schema)
        missing = [key for key in required_keys if not data.get(key)]
        if missing:
            raise serializers.ValidationError({"data": f"Missing required answers for: {', '.join(missing)}"})
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user if self.context.get("request") else None
        return FormSubmission.objects.create(created_by=user, **validated_data)
