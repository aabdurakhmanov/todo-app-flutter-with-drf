from django.contrib import admin
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Todo Project API",
        default_version='v1',
        description="MY todo app describtion",
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('v1/', include('backend.urls')),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),

]
