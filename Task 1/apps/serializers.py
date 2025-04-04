from rest_framework import serializers
from .models import AppInfo

class AppInfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AppInfo
        fields = '__all__'
