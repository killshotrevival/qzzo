from rest_framework import serializers
from .models import profile
from django.contrib.auth.models import User

class profileSerializer(serializers.ModelSerializer):
    class Meta:
        model = profile
        fields = ('place', 'desc')