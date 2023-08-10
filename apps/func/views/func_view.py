import os
import pandas as pd

from rest_framework.viewsets import GenericViewSet
from rest_framework.response import Response
from rest_framework import status
from rest_framework.parsers import MultiPartParser

from apps.func.models.funcionalidades import (
    Cliente,
    RegistroFactura,
    RegistroCredito,
    AbonosCredito,
    ItemFactura,
    InventarioMaquinaria,
    ArchivoExcel
)
from apps.func.serializers.serializers import (
    ClienteSerializer,
    RegistroFacturaSerializer,
    RegistroCreditoSerializer,
    AbonosCreditoSerializer,
    ItemFacturaSerializer,
    InventarioMaquinariaSerializer
)


class ClienteViewSet(GenericViewSet):

    queryset = Cliente.objects.all()
    serializer_class = ClienteSerializer
    search_fields = ['nombre', 'cc_nit']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegistroFacturaViewSet(GenericViewSet):

    queryset = RegistroFactura.objects.all()
    serializer_class = RegistroFacturaSerializer
    search_fields = ['cliente__nombre']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class RegistroCreditoViewSet(GenericViewSet):

    queryset = RegistroCredito.objects.all()
    serializer_class = RegistroCreditoSerializer
    search_fields = ['cliente__nombre']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class AbonosCreditoViewSet(GenericViewSet):

    queryset = AbonosCredito.objects.all()
    serializer_class = AbonosCreditoSerializer
    search_fields = ['cliente__nombre']

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def create(self, request):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

    def retrieve(self, request, pk=None):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        return Response(serializer.data)

    def destroy(self, request, pk=None):
        instance = self.get_object()
        instance.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


class InventarioMaquinariaViewSet(GenericViewSet):
    queryset = InventarioMaquinaria.objects.all()
    serializer_class = InventarioMaquinariaSerializer

    def create(self, request):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        try:
            queryset = self.queryset
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class ItemFacturaViewSet(GenericViewSet):
    queryset = ItemFactura.objects.all()
    serializer_class = ItemFacturaSerializer

    def create(self, request):
        many = isinstance(request.data, list)
        serializer = self.serializer_class(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        try:
            queryset = self.queryset
            serializer = self.serializer_class(queryset, many=True)
            return Response(serializer.data)
        except Exception as e:
            return Response({"error": str(e)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class SubirExcelViewSet(GenericViewSet):
    queryset = ArchivoExcel.objects.all()
    parser_classes = (MultiPartParser, )

    def create(self, request, *args, **kwargs):
        archivo_excel = request.data['archivo']

        extension = os.path.splitext(archivo_excel.name)[1]
        valid_extensions = ['.xlsx', '.xls', '.csv']

        if extension not in valid_extensions:
            return Response(
                {'error': 'Formato de archivo no soportado. Por favor, suba un archivo Excel o CSV.'},
                status=status.HTTP_400_BAD_REQUEST
            )

        if extension == '.csv':
            df = pd.read_csv(archivo_excel)
        else:
            df = pd.read_excel(archivo_excel, sheet_name='Inventario Maquinaria', engine='openpyxl')

        for index, row in df.iterrows():
            InventarioMaquinaria.objects.create(
                item=row['Item'],
                fecha=row['Fecha'],
                equipo=row['Equipo'],
                marca=row['Marca'],
                modelo=row['Modelo'],
                descripcion=row['Descripcion'],
                cantidad=row['Cantidad'],
                centro_costos=row['Centro de Costos'],
                costo_unitario=row['Costo Unitario'],
                costo_peritaje=row['Costo peritaje'],
                costo_entrada=row['Costo Entrada']
            )

        archivo_excel.delete()

        return Response({'message': 'Archivo procesado con éxito'}, status=status.HTTP_201_CREATED)
