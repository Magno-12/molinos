from django.db.models import Sum
from datetime import datetime

from apps.func.models.funcionalidades import (
    CuadroEstadistico, InformeComportamiento, CostosProduccion, VentasDia, 
    GastosTaller, CajaAnticipos, ComparativoIngresosCompras, RegistroMaterial, 
    RegistroCompra, Gasto, GastoConstruccion, CajaSkyCreditoSky,
    CarteraPagar, CuentasPorPagar, SalidaMateriaPrima, InventarioStock, 
    EntradaMateriaPrima, InventarioMaquinaria,
    OtrosInventarioStockEntra, PedidoMateriaPrima, CuentasProveedores
    )

def calcular_ventas_por_mes():
    mes_actual = datetime.now().month
    ventas_por_mes = CuadroEstadistico.objects.filter(mes__lte=mes_actual).\
        aggregate(total_ventas=Sum('ventas_por_mes'))
    return ventas_por_mes['total_ventas'] or 0

def calcular_ponderado_materia_prima():
    ponderado_materia_prima = CuadroEstadistico.objects.aggregate(ponderado=Sum('ponderado_materia_prima'))
    return ponderado_materia_prima['ponderado'] or 0

def calcular_subtotal_ganancias():
    subtotal_ganancias = CuadroEstadistico.objects.aggregate(subtotal=Sum('subtotal_ganancias'))
    return subtotal_ganancias['subtotal'] or 0

def calcular_costos_produccion():
    costos_produccion = CuadroEstadistico.objects.aggregate(total_costos=Sum('costos_produccion'))
    return costos_produccion['total_costos'] or 0

def calcular_total_maquinaria_equipo():
    total_maquinaria_equipo = InformeComportamiento.objects.\
        aggregate(total_maquinaria=Sum('total_maquinaria_equipo'))
    return total_maquinaria_equipo['total_maquinaria'] or 0

def calcular_total_materia_prima():
    total_materia_prima = InformeComportamiento.objects.aggregate(total_materia=Sum('total_materia_prima'))
    return total_materia_prima['total_materia'] or 0

def calcular_total_inventario_maquinaria_equipo():
    total_inventario_maquinaria_equipo = InformeComportamiento.objects.\
        aggregate(total_inventario=Sum('total_inventario_maquinaria_equipo'))
    return total_inventario_maquinaria_equipo['total_inventario'] or 0

def calcular_total_inventario_anterior():
    total_inventario_anterior = InformeComportamiento.objects.\
        aggregate(total_anterior=Sum('total_inventario_anterior'))
    return total_inventario_anterior['total_anterior'] or 0

def calcular_costos_produccion_mes(mes):
    costos_produccion = CostosProduccion.objects.filter(mes=mes).\
        aggregate(total_costos=Sum('costo_produccion'))
    return costos_produccion['total_costos'] or 0

def calcular_total_ventas_dia_maquinaria(maquinaria):
    total_ventas_dia = VentasDia.objects.filter(maquinaria=maquinaria).aggregate(total_ventas=Sum('total'))
    return total_ventas_dia['total_ventas'] or 0

def calcular_acumulado_ingresos():
    acumulado_ingresos = VentasDia.objects.aggregate(acumulado=Sum('acumulado_ingresos'))
    return acumulado_ingresos['acumulado'] or 0

def calcular_total_gastos_taller(taller):
    total_gastos_taller = GastosTaller.objects.filter(taller=taller).\
        aggregate(total_gastos=Sum('total_compras_gastos'))
    return total_gastos_taller['total_gastos'] or 0

def calcular_acumulado_gastos():
    acumulado_gastos = GastosTaller.objects.aggregate(acumulado=Sum('acumulado_gastos'))
    return acumulado_gastos['acumulado'] or 0

def calcular_saldo_inicial_caja():
    caja_anticipos = CajaAnticipos.objects.first()
    if caja_anticipos:
        return caja_anticipos.saldo_inicial_caja
    return 0

def calcular_saldo_caja_anticipos():
    caja_anticipos = CajaAnticipos.objects.first()
    if caja_anticipos:
        return caja_anticipos.saldo_caja_anticipos
    return 0

def calcular_comparativo_ingresos_compras_mes(mes):
    ingresos = VentasDia.objects.filter(fecha__month=mes).aggregate(total_ingresos=Sum('total'))
    compras = GastosTaller.objects.filter(fecha__month=mes).\
        aggregate(total_compras=Sum('total_compras_gastos'))
    return ingresos['total_ingresos'] or 0, compras['total_compras'] or 0

def calcular_total_reintegros_devoluciones():
    total_reintegros_devoluciones = CajaSkyCreditoSky.objects.\
        aggregate(total_reintegros=Sum('reintegros_devoluciones'))
    return total_reintegros_devoluciones['total_reintegros'] or 0

def calcular_total_consignaciones():
    total_consignaciones = CajaSkyCreditoSky.objects.aggregate(total_consignaciones=Sum('consignaciones'))
    return total_consignaciones['total_consignaciones'] or 0

def calcular_total_prestamos():
    total_prestamos = CajaSkyCreditoSky.objects.aggregate(total_prestamos=Sum('prestamos'))
    return total_prestamos['total_prestamos'] or 0

def calcular_total_reintegros_entre_cajas():
    total_reintegros_entre_cajas = CajaSkyCreditoSky.objects.\
        aggregate(total_reintegros_entre_cajas=Sum('reintegros_entre_cajas'))
    return total_reintegros_entre_cajas['total_reintegros_entre_cajas'] or 0

def calcular_cartera_pagare():
    cartera_pagare = CarteraPagar.objects.aggregate(total_cartera=Sum('cartera_pagare'))
    return cartera_pagare['total_cartera'] or 0

def calcular_intereses():
    intereses = CarteraPagar.objects.aggregate(total_intereses=Sum('intereses'))
    return intereses['total_intereses'] or 0

def calcular_total_anticipos():
    total_anticipos = CajaSkyCreditoSky.objects.aggregate(total_anticipos=Sum('anticipos'))
    return total_anticipos['total_anticipos'] or 0

def calcular_total_cuentas_por_pagar():
    total_cuentas_por_pagar = CuentasPorPagar.objects.aggregate(total_cuentas=Sum('monto'))
    return total_cuentas_por_pagar['total_cuentas'] or 0

def calcular_total_salidas_materia_prima(material):
    total_salidas_materia_prima = SalidaMateriaPrima.objects.filter(material=material).\
        aggregate(total_salidas=Sum('cantidad'))
    return total_salidas_materia_prima['total_salidas'] or 0

def calcular_total_inventario_stock(material):
    total_inventario_stock = InventarioStock.objects.filter(material=material).\
        aggregate(total_inventario=Sum('cantidad'))
    return total_inventario_stock['total_inventario'] or 0

def calcular_total_entradas_materia_prima(material):
    total_entradas_materia_prima = EntradaMateriaPrima.objects.filter(material=material).\
        aggregate(total_entradas=Sum('cantidad'))
    return total_entradas_materia_prima['total_entradas'] or 0

def calcular_total_inventario_maquinaria(maquinaria):
    total_inventario_maquinaria = InventarioMaquinaria.objects.filter(maquinaria=maquinaria).\
        aggregate(total_inventario=Sum('cantidad'))
    return total_inventario_maquinaria['total_inventario'] or 0

def calcular_total_otro_inventario_stock():
    total_otro_inventario_stock = OtrosInventarioStockEntra.objects.\
        aggregate(total_inventario=Sum('cantidad'))
    return total_otro_inventario_stock['total_inventario'] or 0

def calcular_total_pedidos_materia_prima(material):
    total_pedidos_materia_prima = PedidoMateriaPrima.objects.filter(material=material).\
        aggregate(total_pedidos=Sum('cantidad'))
    return total_pedidos_materia_prima['total_pedidos'] or 0

def calcular_total_cuentas_proveedores(proveedor):
    total_cuentas_proveedores = CuentasProveedores.objects.filter(proveedor=proveedor).\
        aggregate(total_cuentas=Sum('saldo'))
    return total_cuentas_proveedores['total_cuentas'] or 0
