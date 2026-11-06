from rest_framework import serializers
from .models import Destino


class DestinoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Destino
        fields = '__all__'

    def validate_precio(self, value):
        if value <= 0:
            raise serializers.ValidationError(
                "El precio debe ser mayor que 0."
            )
        return value

    def validate_cupos(self, value):
        if value < 0:
            raise serializers.ValidationError(
                "Los cupos no pueden ser negativos."
            )
        return value