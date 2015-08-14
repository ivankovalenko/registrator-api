# coding: utf-8
from django.conf import settings
from django.conf.urls import include, url
from django.contrib import admin
from django.conf.urls.static import static
from . import views


urlpatterns = [
    url(r'^secret_admin_zone/', include(admin.site.urls)),
    url(r'^acc/', include('acc.urls')),
    url(r'^userlayers/', include('userlayers.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
