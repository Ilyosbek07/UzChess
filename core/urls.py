from xml.etree.ElementInclude import include

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path

from .schema import swagger_urlpatterns

urlpatterns = [
    path("admin/", admin.site.urls),
    path('ckeditor/', include('ckeditor_uploader.urls')),

]

urlpatterns += swagger_urlpatterns

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
