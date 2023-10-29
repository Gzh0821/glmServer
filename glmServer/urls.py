from django.contrib import admin
from django.urls import path, include
from django.views.generic import RedirectView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

schema_view = get_schema_view(
    openapi.Info(
        title="Django-GLM API Document",
        default_version='v1',
        description="A Django-GLM API Document written by Gaozih.",
        terms_of_service="https://github.com/Gzh0821",
        license=openapi.License(name="Apache License 2.0",
                                url="https://www.apache.org/licenses/LICENSE-2.0"),
    ),
    public=True,
    permission_classes=([permissions.AllowAny]),
)

urlpatterns = [
    path('', RedirectView.as_view(url='swagger/', permanent=False)),
    path("admin/", admin.site.urls),
    path('api/archive/', include('archive.urls', namespace='archive')),
    path('api/user/', include('userprofile.urls', namespace='userprofile')),
    path('api/admin/', include('adminfunc.urls', namespace='adminfunc')),
    path('temp/auth/', include('rest_framework.urls')),
    path('swagger<format>/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
