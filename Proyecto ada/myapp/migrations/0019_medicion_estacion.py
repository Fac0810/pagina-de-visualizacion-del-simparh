# Generated by Django 4.1.7 on 2023-03-06 15:04

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0018_remove_medicion_estacion_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='medicion',
            name='estacion',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='myapp.estacion'),
        ),
    ]