# Generated by Django 5.0.2 on 2024-02-12 04:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myAppGestion', '0015_mascotasadopciones'),
    ]

    operations = [
        migrations.AddField(
            model_name='mascotasadopciones',
            name='sexo',
            field=models.CharField(choices=[('H', 'Hembra'), ('M', 'Macho')], default='H', max_length=1),
        ),
    ]
