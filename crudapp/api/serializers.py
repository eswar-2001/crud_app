from rest_framework import serializers
from .models import UserCredential

class UserCredentialSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserCredential
        fields = '__all__'