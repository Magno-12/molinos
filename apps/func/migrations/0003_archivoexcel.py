# Generated by Django 3.2.11 on 2023-08-10 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('func', '0002_auto_20230809_2255'),
    ]

    operations = [
        migrations.CreateModel(
            name='ArchivoExcel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('archivo', models.FileField(blank=True, null=True, upload_to='archivos_excel/')),
                ('subido_en', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
