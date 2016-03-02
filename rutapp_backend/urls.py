from django.conf import settings
from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from rutapp_restapi import views
from rutapp_restapi.errors import error_500, error_404


router = routers.DefaultRouter()
router.register(r'walks', views.WalkViewSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
)

if (settings.DEBUG == True):
    urlpatterns += (
        url(r'^error-500/', error_500, name='error_500'),
        url(r'^error-404/', error_404, name='error_404'),
    )
