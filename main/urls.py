from django.contrib import admin
from django.urls import path
# Three modules for swagger:
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Blog App API",
        default_version="v1",
        description="Blog App API",
        terms_of_service="#",
        contact=openapi.Contact(email="sadi22kislar@gmail.com"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny]
)

urlpatterns = [
    path('admin/', admin.site.urls),
]
