from rest_framework import serializers

from apps.func.models.funcionalidades import (
    Cliente, 
    RegistroFactura, 
    RegistroCredito, 
    AbonosCredito
)


class ClienteSerializer(serializers.ModelSerializer):
    class Meta:
        model = Cliente
        fields = '__all__'


class RegistroFacturaSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroFactura
        fields = '__all__'


class RegistroCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCredito
        fields = '__all__'


class AbonosCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbonosCredito
        fields = '__all__'
