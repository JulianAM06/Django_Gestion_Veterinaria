# Generated by Django 5.0.2 on 2024-02-08 03:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0007_tratamiento_fecha_tratamiento_fkmascota_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='tratamiento',
            name='descripcion',
            field=models.TextField(default='Ingresa descripcion del Tratamiento realizado', max_length=500),
        ),
    ]