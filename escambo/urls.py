from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^home/$', views.home, name='home'),
    url(r'^detalhes/(?P<pk>[0-9]+)/$', views.detalhes, name="detalhes"),
    url(r'^novo/$', views.novo, name="novo"),
    url(r'^sobre/$', views.sobre, name="sobre"),
    url(r'^detalhes/(?P<pk>[0-9]+)/edit/$', views.editar, name='editar'),
    url(r'^$', views.index, name='index'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
