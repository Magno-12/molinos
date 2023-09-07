from django.urls import include, path

from rest_framework import routers

from apps.func.views.func_view import (
    ClienteViewSet,
    RegistroFacturaViewSet,
    RegistroCreditoViewSet,
    AbonosCreditoViewSet,
    InventarioMaquinariaViewSet,
    ItemFacturaViewSet,
    SubirExcelViewSet,
    FinanzasViewSet,
    InventarioStockViewSet
)

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'facturas', RegistroFacturaViewSet, basename='factura')
router.register(r'creditos', RegistroCreditoViewSet, basename='credito')
router.register(r'abonos', AbonosCreditoViewSet, basename='abono')
router.register(r'inventario', InventarioMaquinariaViewSet, basename='inventario')
router.register(r'item_factura', ItemFacturaViewSet, basename='item_factura')
router.register(r'subir_excel', SubirExcelViewSet, basename='subir_excel')
router.register(r'finanzas', FinanzasViewSet, basename='finanzas')
router.register(r'inventariostock', InventarioStockViewSet, basename='inventariostock')

urlpatterns = [
    path('', include(router.urls)),
]
