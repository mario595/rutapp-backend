from time import sleep

from django.conf import settings
from rest_framework import  viewsets

from rutapp_restapi import serializers
from rutapp_restapi.models import Walk


class WalkViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = Walk.objects.all()
    
    def get_serializer_class(self):
        if self.action == 'list':
            return serializers.WalkSummarySerializer
        if self.action == 'retrieve':
            return serializers.WalkDetailSerializer
        
    def initialize_request(self, request, *args, **kwargs):
        if (settings.DEBUG):
            if ('delay' in request.GET):
                try:
                    delay = int(request.GET['delay'])
                    if (delay <= 30):
                        sleep(delay)
                except:
                    pass
        return super(WalkViewSet, self).initialize_request(request, *args, **kwargs)