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
    ArchivoExcel,
    CuadroEstadistico,
    InformeComportamiento,
    CostosProduccion,
    InventarioStock
)
from apps.func.serializers.serializers import (
    ClienteSerializer,
    RegistroFacturaSerializer,
    RegistroCreditoSerializer,
    AbonosCreditoSerializer,
    ItemFacturaSerializer,
    InventarioMaquinariaSerializer,
    InventarioStockSerializer
)
from apps.func.utils import generar_resumen_financiero

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
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


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


class FinanzasViewSet(GenericViewSet):

    def list(self, request):

        cuadros = CuadroEstadistico.objects.all()
        meses = [cuadro.mes for cuadro in cuadros]
        ventas_por_mes = [cuadro.ventas_por_mes for cuadro in cuadros]
        ponderado_materia_prima = [cuadro.ponderado_materia_prima for cuadro in cuadros]
        costos_produccion = [cuadro.costos_produccion for cuadro in cuadros]
        rentabilidad_neta = [cuadro.rentabilidad_neta for cuadro in cuadros]

        informes = InformeComportamiento.objects.all()
        total_maquinaria_equipo = [informe.total_maquinaria_equipo for informe in informes]
        total_materia_prima = [informe.total_materia_prima for informe in informes]

        costos = CostosProduccion.objects.all()
        costo_fijo = [costo.costo_fijo for costo in costos]
        costo_variable = [costo.costo_variable for costo in costos]

        total_ingresos = ventas_por_mes
        total_egresos = [
            ponderado + costo_prod + maquinaria + materia + fijo + variable for ponderado, costo_prod,
            maquinaria, materia, fijo, variable in zip(
                ponderado_materia_prima, costos_produccion, total_maquinaria_equipo, total_materia_prima,
                costo_fijo, costo_variable
            )
        ]

        data = {
            "meses": meses,
            "ventas_por_mes": ventas_por_mes,
            "ponderado_materia_prima": ponderado_materia_prima,
            "costos_produccion": costos_produccion,
            "rentabilidad_neta": rentabilidad_neta,
            "total_maquinaria_equipo": total_maquinaria_equipo,
            "total_materia_prima": total_materia_prima,
            "costo_fijo": costo_fijo,
            "costo_variable": costo_variable,
            "total_ingresos": total_ingresos,
            "total_egresos": total_egresos
        }

        return Response(data)


class InventarioStockViewSet(GenericViewSet):
    queryset = InventarioStock.objects.all()
    serializer_class = InventarioStockSerializer

    def create(self, request):
        many = isinstance(request.data, list)
        serializer = self.serializer_class(data=request.data, many=many)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def list(self, request):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)


class ResumenFinancieroViewSet(GenericViewSet):

    def list(self, request):
        resumen = generar_resumen_financiero()
        return Response(resumen, status=status.HTTP_200_OK)
