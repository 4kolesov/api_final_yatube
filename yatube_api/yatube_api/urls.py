from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.views.generic import TemplateView
from django.conf.urls.static import static

from api import urls

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(urls)),
    path(
        'redoc/',
        TemplateView.as_view(template_name='redoc.html'),
        name='redoc'
    ),
]
if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL, document_root=settings.MEDIA_ROOT
    )
    urlpatterns += static(
        settings.STATIC_URL, document_root=settings.STATIC_ROOT
    )