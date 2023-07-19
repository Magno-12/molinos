from django.urls import include, path

from rest_framework import routers

from apps.func.views.func_view import (
    ClienteViewSet,
    RegistroFacturaViewSet,
    RegistroCreditoViewSet,
    AbonosCreditoViewSet,
)

router = routers.DefaultRouter()
router.register(r'clientes', ClienteViewSet, basename='cliente')
router.register(r'facturas', RegistroFacturaViewSet, basename='factura')
router.register(r'creditos', RegistroCreditoViewSet, basename='credito')
router.register(r'abonos', AbonosCreditoViewSet, basename='abono')

urlpatterns = [
    path('', include(router.urls)),
]
