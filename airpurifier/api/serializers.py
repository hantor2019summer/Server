from rest_framework import serializers
from .models import *

class DustSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fine_Dust
        fields = ("id", "density", "created_date")

class SchSerializer(serializers.ModelSerializer) :
    class Meta:
        model = SwitchLog
        fields = ("id", "state", "created_date")


