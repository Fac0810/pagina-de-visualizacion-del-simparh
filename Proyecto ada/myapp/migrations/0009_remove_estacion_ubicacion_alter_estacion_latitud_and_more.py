# Generated by Django 4.1.7 on 2023-03-02 15:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0008_alter_estacion_desde_alter_estacion_fuente_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='estacion',
            name='ubicacion',
        ),
        migrations.AlterField(
            model_name='estacion',
            name='latitud',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=15, null=True),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='longitud',
            field=models.DecimalField(blank=True, decimal_places=12, max_digits=15, null=True),
        ),
    ]
