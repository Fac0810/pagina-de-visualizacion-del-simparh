# Generated by Django 4.1.7 on 2023-03-06 15:02

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0015_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Asunto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('tipo', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='Contacto',
            fields=[
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True)),
                ('ciudad', models.CharField(max_length=100, null=True)),
                ('email', models.EmailField(max_length=100, null=True)),
                ('telefono', models.DecimalField(decimal_places=3, max_digits=15, null=True)),
                ('mensaje', models.CharField(max_length=950, null=True)),
                ('asunto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.asunto')),
            ],
        ),
    ]
