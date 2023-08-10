from rest_framework import serializers

from apps.func.models.funcionalidades import (
    Cliente,
    RegistroFactura,
    RegistroCredito,
    AbonosCredito,
    ItemFactura,
    InventarioMaquinaria
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


class InventarioMaquinariaSerializer(serializers.ModelSerializer):
    class Meta:
        model = InventarioMaquinaria
        fields = '__all__'

class ItemFacturaSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = ItemFactura
        fields = ['id', 'cantidad', 'producto', 'precio', 'total']