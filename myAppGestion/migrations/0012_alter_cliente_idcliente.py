# Generated by Django 5.0.2 on 2024-02-10 17:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0011_alter_cliente_idcliente'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cliente',
            name='idCliente',
            field=models.AutoField(primary_key=True, serialize=False),
        ),
    ]
