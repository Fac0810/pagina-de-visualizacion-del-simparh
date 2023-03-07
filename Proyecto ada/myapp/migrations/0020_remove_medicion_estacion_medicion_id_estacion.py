# Generated by Django 4.1.7 on 2023-03-06 15:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0019_medicion_estacion'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='medicion',
            name='estacion',
        ),
        migrations.AddField(
            model_name='medicion',
            name='id_estacion',
            field=models.ForeignKey(default='0000', on_delete=django.db.models.deletion.CASCADE, to='myapp.estacion'),
        ),
    ]
