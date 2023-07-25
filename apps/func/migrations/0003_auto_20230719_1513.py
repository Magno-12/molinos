# Generated by Django 3.2.11 on 2023-07-19 15:13

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('func', '0002_abonoscredito_registrocredito_registrofactura'),
    ]

    operations = [
        migrations.CreateModel(
            name='Cliente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(db_index=True, max_length=100)),
                ('cc_nit', models.CharField(max_length=20, unique=True)),
                ('telefono', models.CharField(max_length=30)),
                ('correo_electronico', models.EmailField(max_length=254)),
            ],
            options={
                'verbose_name': 'Cliente',
                'verbose_name_plural': 'Clientes',
            },
        ),
        migrations.RemoveField(
            model_name='abonoscredito',
            name='cc_nit',
        ),
        migrations.RemoveField(
            model_name='abonoscredito',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='abonoscredito',
            name='nombre',
        ),
        migrations.RemoveField(
            model_name='abonoscredito',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='registrocredito',
            name='cc_nit',
        ),
        migrations.RemoveField(
            model_name='registrocredito',
            name='telefono',
        ),
        migrations.RemoveField(
            model_name='registrofactura',
            name='cc_nit',
        ),
        migrations.RemoveField(
            model_name='registrofactura',
            name='correo_electronico',
        ),
        migrations.RemoveField(
            model_name='registrofactura',
            name='telefono',
        ),
        migrations.AlterField(
            model_name='abonoscredito',
            name='credito',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='abonos', to='func.registrocredito'),
        ),
        migrations.AddIndex(
            model_name='registrocredito',
            index=models.Index(fields=['fecha', 'cliente', 'estado', 'forma_de_pago'], name='func_regist_fecha_dbc249_idx'),
        ),
        migrations.AddIndex(
            model_name='registrofactura',
            index=models.Index(fields=['fecha', 'cliente', 'forma_de_pago'], name='func_regist_fecha_191207_idx'),
        ),
        migrations.AddField(
            model_name='abonoscredito',
            name='cliente',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='func.cliente'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='registrocredito',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='func.cliente'),
        ),
        migrations.AlterField(
            model_name='registrofactura',
            name='cliente',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='func.cliente'),
        ),
    ]