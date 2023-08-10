import uuid
from datetime import date
from django.db import models


class CuadroEstadistico(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mes = models.CharField(max_length=20)
    total_maquinaria_equipo = models.DecimalField(max_digits=10, decimal_places=2)
    total_materia_prima = models.DecimalField(max_digits=10, decimal_places=2)
    total_inventario_maquinaria_equipo = models.DecimalField(max_digits=10, decimal_places=2)
    total_inventario_anterior = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Informe de Comportamiento'
        verbose_name_plural = 'Informes de Comportamiento'


class CostosProduccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mes = models.CharField(max_length=20)
    costo_produccion = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Costos de Producción'
        verbose_name_plural = 'Costos de Producción'


class VentasDia(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    taller = models.CharField(max_length=50)
    saldo_pendiente = models.DecimalField(max_digits=10, decimal_places=2)
    subtotal_compras_gastos = models.DecimalField(max_digits=10, decimal_places=2)
    total_compras_gastos = models.DecimalField(max_digits=10, decimal_places=2)
    acumulado_gastos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Gastos del Taller'
        verbose_name_plural = 'Gastos del Taller'


class CajaAnticipos(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    saldo_inicial_caja = models.DecimalField(max_digits=10, decimal_places=2)
    otros_gastos = models.DecimalField(max_digits=10, decimal_places=2)
    saldo_caja_anticipos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Caja de Anticipos'
        verbose_name_plural = 'Cajas de Anticipos'


class ComparativoIngresosCompras(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    mes = models.CharField(max_length=20)
    ingresos = models.DecimalField(max_digits=10, decimal_places=2)
    compras = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Comparativo Ingresos vs Compras'
        verbose_name_plural = 'Comparativos Ingresos vs Compras'


class RegistroMaterial(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=50)
    dimensiones = models.CharField(max_length=50)
    kilogramos = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Registro de Material'
        verbose_name_plural = 'Registros de Materiales'


class RegistroCompra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    centro_costos = models.CharField(max_length=50)
    fecha = models.DateField()
    subtotal = models.DecimalField(max_digits=10, decimal_places=2)
    total = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Registro de Compra'
        verbose_name_plural = 'Registros de Compras'


class Gasto(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Gasto'
        verbose_name_plural = 'Gastos'


class GastoConstruccion(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Gasto Construcción'
        verbose_name_plural = 'Gastos Construcción'


class CajaSkyCreditoSky(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
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
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre_persona = models.CharField(max_length=50)
    deudas_empresa = models.DecimalField(max_digits=10, decimal_places=2)
    abonos_credito = models.DecimalField(max_digits=10, decimal_places=2)
    intereses = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cartera Pagaré'
        verbose_name_plural = 'Carteras Pagaré'


class CuentasPorPagar(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=100)
    monto = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cuenta por Pagar'
        verbose_name_plural = 'Cuentas por Pagar'


class SalidaMateriaPrima(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Salida de Materia Prima'
        verbose_name_plural = 'Salidas de Materias Primas'


class InventarioStock(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Inventario Stock'
        verbose_name_plural = 'Inventarios Stock'


class EntradaMateriaPrima(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Entrada de Materia Prima'
        verbose_name_plural = 'Entradas de Materias Primas'


class InventarioMaquinaria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    maquinaria = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Inventario Maquinaria'
        verbose_name_plural = 'Inventarios Maquinaria'


class OtrosInventarioStockEntra(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    descripcion = models.CharField(max_length=100)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Otros Inventario Stock - Entra'
        verbose_name_plural = 'Otros Inventarios Stock - Entra'


class PedidoMateriaPrima(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    material = models.CharField(max_length=50)
    cantidad = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Pedido de Materia Prima'
        verbose_name_plural = 'Pedidos de Materias Primas'


class CuentasProveedores(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    proveedor = models.CharField(max_length=50)
    saldo = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Cuenta Proveedor'
        verbose_name_plural = 'Cuentas Proveedores'


class Cliente(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    nombre = models.CharField(max_length=100, db_index=True)
    cc_nit = models.CharField(max_length=20, unique=True)
    telefono = models.CharField(max_length=30)
    correo_electronico = models.EmailField()

    class Meta:
        verbose_name = 'Cliente'
        verbose_name_plural = 'Clientes'


class RegistroFactura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    tipo = models.CharField(max_length=10)
    forma_de_pago = models.CharField(max_length=20)
    direccion = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Registro de Factura'
        verbose_name_plural = 'Registros de Facturas'
        indexes = [
            models.Index(fields=['fecha', 'cliente', 'forma_de_pago']),
        ]

    def __str__(self):
        return f'Factura {self.factura_id} - Cliente: {self.cliente.nombre}'

class InventarioMaquinaria(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    item = models.PositiveIntegerField(verbose_name="Item", unique=True, default=0)
    fecha = models.DateField(verbose_name="Fecha", default=date.today)
    equipo = models.CharField(max_length=100, verbose_name="Equipo", default="")
    marca = models.CharField(max_length=100, verbose_name="Marca", default="")
    modelo = models.CharField(max_length=100, verbose_name="Modelo", default="")
    descripcion = models.TextField(verbose_name="Descripcion", default="")
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad", default=0)
    centro_costos = models.CharField(max_length=100, verbose_name="Centro de Costos", default="")
    costo_unitario = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Unitario", default=0)
    costo_peritaje = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo peritaje", default=0)
    costo_entrada = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Costo Entrada", default=0)

    class Meta:
        verbose_name = "Inventario de Maquinaria"
        verbose_name_plural = "Inventario de Maquinarias"


class ItemFactura(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    cantidad = models.PositiveIntegerField(verbose_name="Cantidad")
    producto = models.ForeignKey(InventarioMaquinaria, on_delete=models.CASCADE, verbose_name="Producto", null=True, blank=True)
    add_product = models.CharField(max_length=255, verbose_name="Producto", null=True, blank=True)
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio", default=0)
    total = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total")
    registro_factura = models.ForeignKey(RegistroFactura, on_delete=models.CASCADE, related_name='items')


class RegistroCredito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    fecha = models.DateField()
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    detalles = models.CharField(max_length=50)
    valor = models.DecimalField(max_digits=20, decimal_places=2)
    abono = models.DecimalField(max_digits=20, decimal_places=2, default=0)
    estado = models.CharField(max_length=10)
    forma_de_pago = models.CharField(max_length=20)
    tasa_interes = models.DecimalField(max_digits=20, decimal_places=2)
    fecha_vencimiento = models.DateField()

    class Meta:
        verbose_name = 'Registro de Crédito'
        verbose_name_plural = 'Registros de Créditos'
        indexes = [
            models.Index(fields=['fecha', 'cliente', 'estado', 'forma_de_pago']),
        ]


class AbonosCredito(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    credito = models.ForeignKey(RegistroCredito, related_name='abonos', on_delete=models.CASCADE)
    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE)
    forma_de_pago = models.CharField(max_length=20)
    valor_abono = models.DecimalField(max_digits=20, decimal_places=2)

    def save(self, *args, **kwargs):
        self.credito.abono += self.valor_abono
        self.credito.save()
        super().save(*args, **kwargs)


class ArchivoExcel(models.Model):
    archivo = models.FileField(upload_to='archivos_excel/', blank=True, null=True)
    subido_en = models.DateTimeField(auto_now_add=True)
