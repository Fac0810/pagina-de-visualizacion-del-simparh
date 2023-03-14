# Generated by Django 4.1.7 on 2023-03-14 15:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0022_remove_contacto_ciudad_contacto_localidad_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='estacion',
            name='desde',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='fuente',
            field=models.CharField(max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='hasta',
            field=models.DateField(null=True),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='nombre',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='estacion',
            name='ubicacion',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
