# Generated by Django 2.2.6 on 2021-04-20 19:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0003_auto_20210409_1838'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mascota',
            name='foto',
            field=models.ImageField(default='static/images/fondo.jpg', upload_to='static/images'),
        ),
    ]
