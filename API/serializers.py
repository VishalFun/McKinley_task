from rest_framework import serializers
from . import models

class UserATMSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.UserATM
        fields = "__all__"

class UserAuthenticSerializer(serializers.Serializer):
    card = serializers.CharField()
    pin = serializers.CharField()

class UserAmountSerial(serializers.Serializer):
    card = serializers.CharField()
    pin = serializers.CharField()
    balance = serializers.CharField()

