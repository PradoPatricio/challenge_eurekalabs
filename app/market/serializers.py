from rest_framework import serializers


class MarketDataSerializer(serializers.Serializer):
    symbol = serializers.CharField()
    open = serializers.CharField()
    higher = serializers.CharField()
    lower = serializers.CharField()
    variation = serializers.CharField()
