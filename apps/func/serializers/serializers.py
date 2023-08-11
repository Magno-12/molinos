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


class ItemFacturaSerializer(serializers.ModelSerializer):
    total = serializers.DecimalField(max_digits=10, decimal_places=2, read_only=True)
    class Meta:
        model = ItemFactura
        fields = ['id', 'cantidad', 'producto', 'add_product', 'precio', 'total']


class RegistroFacturaSerializer(serializers.ModelSerializer):
    items = ItemFacturaSerializer(many=True, write_only=True, required=False)

    class Meta:
        model = RegistroFactura
        fields = '__all__'

    def create(self, validated_data):
        items_data = validated_data.pop('items', [])
        registro_factura = RegistroFactura.objects.create(**validated_data)
        for item_data in items_data:
            ItemFactura.objects.create(registro_factura=registro_factura, **item_data)
        return registro_factura



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

