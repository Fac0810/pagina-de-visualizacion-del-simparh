# Generated by Django 5.0.1 on 2024-02-20 17:39

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0026_rename_ultima_coneccion_usuario_ultima_conexion'),
    ]

    operations = [
        migrations.CreateModel(
            name='TipoUsuario',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=60)),
            ],
        ),
        migrations.AddField(
            model_name='usuario',
            name='activo',
            field=models.BooleanField(default=True),
        ),
        migrations.AddField(
            model_name='usuario',
            name='superuser',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='localidad',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
        migrations.AlterField(
            model_name='contacto',
            name='partido',
            field=models.CharField(max_length=100),
        ),
        migrations.AddField(
            model_name='usuario',
            name='tipo_usuario_id',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.SET_DEFAULT, to='myapp.tipousuario'),
        ),
    ]
