"""settings URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.conf import settings
from django.conf.urls.static import static
from django.conf.urls import handler404, handler500
from app.views import custom_exceptions, views
from app.views.api_views import *
from authorization.views import *

from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from django.views.static import serve
from django.conf.urls import url
import notifications.urls

schema_view = get_schema_view(
   openapi.Info(
      title="Console-Check API",
      default_version='v1',
      description="console-check",
   ),
#    public=True,
   permission_classes=[permissions.IsAdminUser],
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    path('authorization/', include('authorization.urls')),
    path('swagger-json/', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    path('products/', ProductList.as_view()),
    path('product-type/', ProductTypeList.as_view()),
    # path('notifications/', include(notifications.urls, namespace='notifications')),
    url('^inbox/notifications/', include(notifications.urls, namespace='notifications')),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
    url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
    path('unread_notifications/', unread_notifications, name='unread_notifications'),
] # + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler500 = custom_exceptions.error500
handler404 = custom_exceptions.error404