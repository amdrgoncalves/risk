from rest_framework import serializers
from .models import Risk, RiskField


class RiskAllSerializer(serializers.ModelSerializer):
    class Meta:
        model = Risk
        fields = ('id','name')

class RiskFieldSerializer(serializers.ModelSerializer):
    #translate type tp human radable version
    type = serializers.CharField(source='get_type_display')
    class Meta:
        model = RiskField
        fields = ('id','type','caption','options')

class Risk1Serializer(serializers.ModelSerializer):
    risk_field = RiskFieldSerializer(many=True,read_only=True)
    class Meta:
        model = Risk
        fields = ('name', 'risk_field')
