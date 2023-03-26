from django.contrib import admin
from django.urls import path, include
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
    path("users/", include("users.urls")),
    path("api/", include("blog.urls")),
    # url path for swagger:
    path("swagger(<format>\.json|\yaml)", schema_view.without_ui(cache_timeout=0), name="schema-json"),
    path("swagger/", schema_view.with_ui("redoc", cache_timeout=0), name="schemaredoc"),
    path("redoc/", schema_view.with_ui("redoc", cache_timeout=0), name="schemaredoc"),
    path('__debug__/', include('debug_toolbar.urls')),
]
