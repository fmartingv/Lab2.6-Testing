from rest_framework import serializers
from .models import Burro

class BurroSerializer(serializers.ModelSerializer):
    class Meta:
        model = Burro
        fields = ['id', 'nombre', 'edad', 'color', 'peso']