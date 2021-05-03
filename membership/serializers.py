# serializers.py
from rest_framework import serializers
from .models import Membership


class MemebershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = ['name', 'phone_number', 'address', 'gender', 'height', 'weight']
