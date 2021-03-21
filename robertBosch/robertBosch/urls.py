"""robertBosch URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from rest_framework_jwt.views import obtain_jwt_token, refresh_jwt_token, verify_jwt_token


schema_view = get_schema_view(
   openapi.Info(
      title="Mentorship API",
      default_version='v1',
      description="post questions to Mentor",
   ),
   public=False,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('mentorship/', include('mentorship.urls')),
   	path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
   	path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
   	path('api-token-auth/', obtain_jwt_token),
   	path('api-token-refresh/', refresh_jwt_token),
   	path('api-token-verify/', verify_jwt_token),
]
