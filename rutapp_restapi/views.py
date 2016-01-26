from rest_framework import viewsets

from rutapp_restapi.models import Walk
from rutapp_restapi.serializers import WalkSummarySerializer


class WalkSet(viewsets.ModelViewSet):
    queryset = Walk.objects.all()
    serializer_class = WalkSummarySerializer
    http_method_names = ['get']
