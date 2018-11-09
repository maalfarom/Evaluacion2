# Generated by Django 2.1.3 on 2018-11-08 22:28

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('EvaluacionDosApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='automovil',
            name='Color',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='automovil',
            name='FechaPublicacion',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
        migrations.AlterField(
            model_name='automovil',
            name='Marca',
            field=models.CharField(max_length=40),
        ),
        migrations.AlterField(
            model_name='automovil',
            name='Modelo',
            field=models.CharField(max_length=40),
        ),
    ]