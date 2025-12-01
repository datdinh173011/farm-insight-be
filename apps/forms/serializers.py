from typing import Iterable, Set

from rest_framework import serializers

from .models import FormSubmission, FormTemplate


class FormTemplateSerializer(serializers.ModelSerializer):
    class Meta:
        model = FormTemplate
        fields = ("id", "template_type", "title", "description",
                  "source_pdf", "schema", "created_at", "updated_at")
        read_only_fields = fields


def _collect_required_keys(schema: dict) -> Set[str]:
    required: Set[str] = set()

    def visit(field: dict):
        if field.get("required"):
            key = field.get("key")
            if key:
                required.add(key)
        nested_fields: Iterable[dict] = field.get(
            "fields", []) or field.get("columns", [])
        for nested in nested_fields:
            visit(nested)

    for section in schema.get("sections", []):
        for field in section.get("fields", []):
            visit(field)
    return required


def _data_contains_key(data: dict, key: str) -> bool:
    """Check if a required key exists with a truthy value at top-level or in list-of-dicts."""
    if data.get(key):
        return True
    for value in data.values():
        if isinstance(value, list):
            for row in value:
                if isinstance(row, dict) and row.get(key):
                    return True
    return False


class FormSubmissionSerializer(serializers.ModelSerializer):
    template = serializers.PrimaryKeyRelatedField(
        queryset=FormTemplate.objects.all(), required=False)
    template_type = serializers.CharField()
    nam_sinh = serializers.IntegerField(required=False, allow_null=True, min_value=0)

    class Meta:
        model = FormSubmission
        fields = (
            "id",
            "template",
            "template_type",
            "ho_ten",
            "nam_sinh",
            "so_dien_thoai",
            "thon",
            "xa",
            "tinh",
            "data",
            "status",
            "created_at",
            "updated_at",
        )
        read_only_fields = ("created_at", "updated_at", "template")

    def validate(self, attrs):
        template_type = attrs.get("template_type")
        try:
            template = FormTemplate.objects.get(template_type=template_type)
        except FormTemplate.DoesNotExist:
            raise serializers.ValidationError(
                {"template_type": "Template type not found"})

        data = attrs.get("data") or {}
        required_keys = _collect_required_keys(template.schema)
        for key in required_keys:
            if not _data_contains_key(data, key):
                data[key] = ""

        attrs["data"] = data
        attrs["template"] = template
        attrs["template_type"] = template.template_type
        return attrs

    def create(self, validated_data):
        user = self.context["request"].user if self.context.get("request") else None
        if user and user.is_anonymous:
            user = None
        return FormSubmission.objects.create(created_by=user, **validated_data)
