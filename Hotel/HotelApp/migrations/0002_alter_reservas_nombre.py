# Generated by Django 5.1.3 on 2024-12-01 20:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HotelApp', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reservas',
            name='nombre',
            field=models.CharField(max_length=100),
        ),
    ]
