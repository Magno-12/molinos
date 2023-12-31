# Generated by Django 3.2.11 on 2023-08-10 03:55

import datetime
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    dependencies = [
        ('func', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inventariomaquinaria',
            options={'verbose_name': 'Inventario de Maquinaria', 'verbose_name_plural': 'Inventario de Maquinarias'},
        ),
        migrations.RemoveField(
            model_name='inventariomaquinaria',
            name='maquinaria',
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='centro_costos',
            field=models.CharField(default='', max_length=100, verbose_name='Centro de Costos'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='costo_entrada',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo Entrada'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='costo_peritaje',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo peritaje'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='costo_unitario',
            field=models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Costo Unitario'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='descripcion',
            field=models.TextField(default='', verbose_name='Descripcion'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='equipo',
            field=models.CharField(default='', max_length=100, verbose_name='Equipo'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='fecha',
            field=models.DateField(default=datetime.date.today, verbose_name='Fecha'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='item',
            field=models.PositiveIntegerField(default=0, unique=True, verbose_name='Item'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='marca',
            field=models.CharField(default='', max_length=100, verbose_name='Marca'),
        ),
        migrations.AddField(
            model_name='inventariomaquinaria',
            name='modelo',
            field=models.CharField(default='', max_length=100, verbose_name='Modelo'),
        ),
        migrations.AlterField(
            model_name='inventariomaquinaria',
            name='cantidad',
            field=models.PositiveIntegerField(default=0, verbose_name='Cantidad'),
        ),
        migrations.CreateModel(
            name='ItemFactura',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cantidad', models.PositiveIntegerField(verbose_name='Cantidad')),
                ('precio', models.DecimalField(decimal_places=2, default=0, max_digits=10, verbose_name='Precio')),
                ('total', models.DecimalField(decimal_places=2, max_digits=10, verbose_name='Total')),
                ('producto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='func.inventariomaquinaria', verbose_name='Producto')),
            ],
        ),
    ]
