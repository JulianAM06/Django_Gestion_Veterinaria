# Generated by Django 5.0.2 on 2024-02-12 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0017_mascotasadopciones_especie'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascotasadopciones',
            name='especie',
            field=models.CharField(choices=[('Perro', 'Perro'), ('Gato', 'Gato')], default='Perro', max_length=5),
        ),
    ]