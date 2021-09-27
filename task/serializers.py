from rest_framework import serializers
from task.models import *

class ConversionSerializer(serializers.ModelSerializer):
    class Meta:
        model = Conversion
        fields = ('id', 'from_currency_code', 'to_currency_code','from_currency_name','to_currency_name','exchange_rate','created_at')