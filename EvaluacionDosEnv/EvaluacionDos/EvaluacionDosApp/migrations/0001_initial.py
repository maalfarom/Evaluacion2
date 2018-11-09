# Generated by Django 2.1.3 on 2018-11-07 20:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Automovil',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Marca', models.TextField(max_length=40)),
                ('Modelo', models.TextField(max_length=40)),
                ('Anio', models.IntegerField(default=1000, validators=[django.core.validators.MaxValueValidator(2018), django.core.validators.MinValueValidator(1000)])),
                ('Color', models.TextField(max_length=40)),
                ('NumeroPuertas', models.IntegerField(default=2, validators=[django.core.validators.MaxValueValidator(5), django.core.validators.MinValueValidator(2)])),
                ('Descripcion', models.TextField(max_length=200)),
                ('FechaPublicacion', models.DateTimeField(blank=True, null=True)),
                ('Precio', models.IntegerField(default=500000, validators=[django.core.validators.MaxValueValidator(20000000), django.core.validators.MinValueValidator(500000)])),
            ],
        ),
    ]
