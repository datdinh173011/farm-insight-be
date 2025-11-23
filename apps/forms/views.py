from rest_framework import mixins, permissions, viewsets

from .models import FormSubmission, FormTemplate
from .serializers import FormSubmissionSerializer, FormTemplateSerializer


class FormTemplateViewSet(mixins.ListModelMixin, mixins.RetrieveModelMixin, viewsets.GenericViewSet):
    queryset = FormTemplate.objects.all()
    serializer_class = FormTemplateSerializer
    permission_classes = [permissions.IsAuthenticated]


class FormSubmissionViewSet(viewsets.ModelViewSet):
    serializer_class = FormSubmissionSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        queryset = FormSubmission.objects.select_related("template")
        if self.request.user and self.request.user.is_staff:
            base = queryset
        else:
            base = queryset.filter(created_by=self.request.user)

        template_slug = self.request.query_params.get("template")
        if template_slug:
            base = base.filter(template__slug=template_slug)
        status_param = self.request.query_params.get("status")
        if status_param:
            base = base.filter(status=status_param)
        return base
