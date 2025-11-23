from rest_framework import mixins, permissions, viewsets

from .models import FormSubmission, FormTemplate
from .serializers import FormSubmissionSerializer, FormTemplateSerializer


class FormTemplateViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]
    lookup_field = "template_type"


class FormSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = FormSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_permissions(self):
        # Cho phép gửi form hoặc xem chi tiết submission không cần đăng nhập; các thao tác khác yêu cầu auth.
        if self.action in {"create", "retrieve"}:
            return [permissions.AllowAny()]
        return super().get_permissions()

    def get_queryset(self):
        base = FormSubmission.objects.select_related("template")

        template_type = self.request.query_params.get("template_type")
        if template_type:
            base = base.filter(template_type=template_type)
        status_param = self.request.query_params.get("status")
        if status_param:
            base = base.filter(status=status_param)
        return base
