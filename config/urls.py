from django.contrib import admin
from django.urls import include, path
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

from apps.forms.views import FormSubmissionViewSet, FormTemplateViewSet
from apps.accounts.views import RegisterView

router = routers.DefaultRouter()
router.register(r"forms/templates", FormTemplateViewSet, basename="form-template")
router.register(r"forms/submissions", FormSubmissionViewSet, basename="form-submission")

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/auth/register/", RegisterView.as_view(), name="register"),
    path("api/auth/token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/auth/token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/", include(router.urls)),
]
