# Generated by Django 2.2.6 on 2021-04-09 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0002_auto_20210409_1833'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(default='C:/mascotas/mascotas/Apps/redsocial/static/images/fomdo.jpg', upload_to='C:/mascotas/mascotas/Apps/redsocial/static/images'),
        ),
    ]
