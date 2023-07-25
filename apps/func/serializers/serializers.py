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
        fields = ("cliente", "valor", "tipo", "forma_de_pago")


class RegistroCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegistroCredito
        fields = (
            "cliente", 
            "detalles", 
            "valor", 
            "abono", 
            "estado", 
            "forma_de_pago", 
            "tasa_interes", 
            "fecha_vencimiento"
        )


class AbonosCreditoSerializer(serializers.ModelSerializer):
    class Meta:
        model = AbonosCredito
        fields = '__all__'
