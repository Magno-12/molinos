# Generated by Django 3.2.11 on 2023-08-10 03:01

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=255, unique=True, verbose_name='email address')),
                ('username', models.CharField(max_length=30, unique=True)),
                ('full_name', models.CharField(max_length=50)),
                ('role', models.CharField(choices=[('admin', 'Admin'), ('empleado', 'Empleado'), ('facturas', 'Facturas')], default='admin', max_length=20)),
                ('is_active', models.BooleanField(default=True)),
                ('is_staff', models.BooleanField(default=True)),
                ('is_admin', models.BooleanField(default=False)),
                ('is_superuser', models.BooleanField(default=True)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
