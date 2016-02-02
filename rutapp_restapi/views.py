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