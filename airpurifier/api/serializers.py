from rest_framework import serializers
from .models import Fine_Dust

class DustSerializer(serializers.ModelSerializer) :
    class Meta:
        model = Fine_Dust
        fields = ("id", "density", "created_date")



