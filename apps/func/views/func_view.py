from rest_framework import filters, viewsets, mixins

from apps.func.models.funcionalidades import (
    Cliente, 
    RegistroFactura, 
    RegistroCredito, 
    AbonosCredito
)
from apps.func.serializers.serializers import (
    ClienteSerializer, 
    RegistroFacturaSerializer, 
    RegistroCreditoSerializer, 
    AbonosCreditoSerializer
)


class ClienteViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    Return a cliente instance.
    
    list:
    Return all clientes, ordered by most recently joined.
    
    create:
    Create a new cliente.
    
    Error Messages:
    - 400 Bad Request: Invalid data was sent.
    - 404 Not Found: The requested cliente does not exist.
    
    Body:
    - nombre: The name of the cliente.
    - cc_nit: The cc_nit of the cliente.
    - telefono: The phone number of the cliente.
    - correo_electronico: The email of the cliente.
    
    Response:
    - id: The id of the cliente.
    - nombre: The name of the cliente.
    - cc_nit: The cc_nit of the cliente.
    - telefono: The phone number of the cliente.
    - correo_electronico: The email of the cliente.
    """
    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['nombre', 'cc_nit']


class RegistroFacturaViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    Return a factura instance.
    
    list:
    Return all facturas, ordered by most recently joined.
    
    create:
    Create a new factura.
    
    Error Messages:
    - 400 Bad Request: Invalid data was sent.
    - 404 Not Found: The requested factura does not exist.
    
    Body:
    - fecha: The date of the factura.
    - cliente: The id of the cliente.
    - valor: The value of the factura.
    - tipo: The type of the factura.
    - forma_de_pago: The payment method of the factura.
    
    Response:
    - factura_id: The id of the factura.
    - fecha: The date of the factura.
    - cliente: The id of the cliente.
    - valor: The value of the factura.
    - tipo: The type of the factura.
    - forma_de_pago: The payment method of the factura.
    """
    queryset = RegistroFactura.objects.all()
    serializer_class = RegistroFacturaSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente__nombre']


class RegistroCreditoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    Return a credito instance.
    
    list:
    Return all creditos, ordered by most recently joined.
    
    create:
    Create a new credito.
    
    Error Messages:
    - 400 Bad Request: Invalid data was sent.
    - 404 Not Found: The requested credito does not exist.
    
    Body:
    - fecha: The date of the credito.
    - cliente: The id of the cliente.
    - detalles: The details of the credito.
    - valor: The value of the credito.
    - abono: The abono of the credito.
    - estado: The state of the credito.
    - forma_de_pago: The payment method of the credito.
    - tasa_interes: The interest rate of the credito.
    - fecha_vencimiento: The due date of the credito.
    
    Response:
    - id: The id of the credito.
    - fecha: The date of the credito.
    - cliente: The id of the cliente.
    - detalles: The details of the credito.
    - valor: The value of the credito.
    - abono: The abono of the credito.
    - estado: The state of the credito.
    - forma_de_pago: The payment method of the credito.
    - tasa_interes: The interest rate of the credito.
    - fecha_vencimiento: The due date of the credito.
    """
    queryset = RegistroCredito.objects.all()
    serializer_class = RegistroCreditoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente__nombre']


class AbonosCreditoViewSet(mixins.ListModelMixin, mixins.CreateModelMixin, viewsets.GenericViewSet):
    """
    retrieve:
    Return a abono instance.
    
    list:
    Return all abonos, ordered by most recently joined.
    
    create:
    Create a new abono.
    
    Error Messages:
    - 400 Bad Request: Invalid data was sent.
    - 404 Not Found: The requested abono does not exist.
    
    Body:
    - credito: The id of the credito.
    - cliente: The id of the cliente.
    - forma_de_pago: The payment method of the abono.
    - valor_abono: The value of the abono.
    
    Response:
    - id: The id of the abono.
    - credito: The id of the credito.
    - cliente: The id of the cliente.
    - forma_de_pago: The payment method of the abono.
    - valor_abono: The value of the abono.
    """
    queryset = AbonosCredito.objects.all()
    serializer_class = AbonosCreditoSerializer
    filter_backends = [filters.SearchFilter]
    search_fields = ['cliente__nombre']
