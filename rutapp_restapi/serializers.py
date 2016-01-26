from rest_framework import serializers
from .models import Walk

class WalkSummarySerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Walk
        fields = ('id', 'name', 'difficulty')

class WalkSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Walk
        fields = ('id', 'name', 'difficulty', 'length', 'region', 'travel_info')