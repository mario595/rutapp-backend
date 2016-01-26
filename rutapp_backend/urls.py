from django.conf.urls import patterns, include, url
from django.contrib import admin
from rest_framework import routers

from rutapp_restapi import views


router = routers.DefaultRouter()
router.register(r'walks', views.WalkSet)

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^', include(router.urls)),
)
