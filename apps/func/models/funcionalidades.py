from django.db import models


class CuadroEstadistico(models.Model):
    mes = models.CharField(max_length=20)
    ventas_por_mes = models.DecimalField(max_digits=10, decimal_places=2)
    ponderado_materia_prima = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_ganancias = models.DecimalField(max_digits=10, decimal_places=2)
    costos_produccion = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_rentabilidad = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_porcentaje_rentabilidad = models.DecimalField(max_digits=10, decimal_places=2)
    gastos_construccion = models.DecimalField(max_digits=10, decimal_places=2)
    rentabilidad_neta = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_rentabilidad_neta = models.DecimalField(max_digits=10, decimal_places=2)
    crecimiento_ventas_anterior = models.DecimalField(max_digits=10, decimal_places=2)
    porcentaje_crecimiento_anterior = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cuadro Estadístico'
        verbose_name_plural = 'Cuadros Estadísticos'


class InformeComportamiento(models.Model):
    mes = models.CharField(max_length=20)
    total_maquinaria_equipo = models.DecimalField(max_digits=10, decimal_places=2)
    total_materia_prima = models.DecimalField(max_digits=10, decimal_places=2)
    total_inventario_maquinaria_equipo = models.DecimalField(max_digits=10, decimal_places=2)
    total_inventario_anterior = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Informe de Comportamiento'
        verbose_name_plural = 'Informes de Comportamiento'


class CostosProduccion(models.Model):
    mes = models.CharField(max_length=20)
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Costos de Producción'
        verbose_name_plural = 'Costos de Producción'


class VentasDia(models.Model):
    maquinaria = models.CharField(max_length=50)
    fecha = models.DateField()
    comprobante = models.CharField(max_length=50)
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)
    acumulado_ingresos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Ventas del Día'
        verbose_name_plural = 'Ventas del Día'


class GastosTaller(models.Model):
    taller = models.CharField(max_length=50)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_compras_gastos = models.DecimalField(max_digits=10, decimal_places=2)
    total_compras_gastos = models.DecimalField(max_digits=10, decimal_places=2)
    acumulado_gastos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Gastos del Taller'
        verbose_name_plural = 'Gastos del Taller'


class CajaAnticipos(models.Model):
    saldo_inicial_caja = models.DecimalField(max_digits=10, decimal_places=2)
    otros_gastos = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_caja_anticipos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Caja de Anticipos'
        verbose_name_plural = 'Cajas de Anticipos'


class ComparativoIngresosCompras(models.Model):
    mes = models.CharField(max_length=20)
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    compras = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Comparativo Ingresos vs Compras'
        verbose_name_plural = 'Comparativos Ingresos vs Compras'


class RegistroMaterial(models.Model):
    material = models.CharField(max_length=50)
    dimensiones = models.CharField(max_length=50)
    kilogramos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Registro de Material'
        verbose_name_plural = 'Registros de Materiales'


class RegistroCompra(models.Model):
    centro_costos = models.CharField(max_length=50)
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Registro de Compra'
        verbose_name_plural = 'Registros de Compras'


class Gasto(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


class GastoConstruccion(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Gasto Construcción'
        verbose_name_plural = 'Gastos Construcción'


class CajaSkyCreditoSky(models.Model):
    reintegros_devoluciones = models.DecimalField(max_digits=10, decimal_places=2)
    consignaciones = models.DecimalField(max_digits=10, decimal_places=2)
    prestamos = models.DecimalField(max_digits=10, decimal_places=2)
    reintegros_entre_cajas = models.DecimalField(max_digits=10, decimal_places=2)
    nombre_encargado_prestamo = models.CharField(max_length=50)
    cartera_pagare = models.DecimalField(max_digits=10, decimal_places=2)
    intereses = models.DecimalField(max_digits=10, decimal_places=2)
    anticipos = models.DecimalField(max_digits=10, decimal_places=2)
    cuentas_por_pagar = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Caja Sky - Crédito Sky'
        verbose_name_plural = 'Cajas Sky - Crédito Sky'


class CarteraPagar(models.Model):
    nombre_persona = models.CharField(max_length=50)
    deudas_empresa = models.DecimalField(max_digits=10, decimal_places=2)
    abonos_credito = models.DecimalField(max_digits=10, decimal_places=2)
    intereses = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cartera Pagaré'
        verbose_name_plural = 'Carteras Pagaré'


class CuentasPorPagar(models.Model):
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cuenta por Pagar'
        verbose_name_plural = 'Cuentas por Pagar'


class SalidaMateriaPrima(models.Model):
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Salida de Materia Prima'
        verbose_name_plural = 'Salidas de Materias Primas'


class InventarioStock(models.Model):
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Inventario Stock'
        verbose_name_plural = 'Inventarios Stock'


class EntradaMateriaPrima(models.Model):
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Entrada de Materia Prima'
        verbose_name_plural = 'Entradas de Materias Primas'


class InventarioMaquinaria(models.Model):
    maquinaria = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Inventario Maquinaria'
        verbose_name_plural = 'Inventarios Maquinaria'


class OtrosInventarioStockEntra(models.Model):
    descripcion = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Otros Inventario Stock - Entra'
        verbose_name_plural = 'Otros Inventarios Stock - Entra'


class PedidoMateriaPrima(models.Model):
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Pedido de Materia Prima'
        verbose_name_plural = 'Pedidos de Materias Primas'


class CuentasProveedores(models.Model):
    proveedor = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cuenta Proveedor'
        verbose_name_plural = 'Cuentas Proveedores'
