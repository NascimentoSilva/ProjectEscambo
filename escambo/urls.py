from django.conf.urls import url, include
from django.contrib import admin
from . import views
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^detalhes/(?P<pk>[0-9]+)/$', views.detalhes, name="detalhes"),
    url(r'^novo/$', views.novo, name="novo"),
    url(r'^sobre/$', views.sobre, name="sobre"),
]
