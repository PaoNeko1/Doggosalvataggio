# Generated by Django 3.1.2 on 2021-05-04 02:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0016_remove_coment_rut_comentario'),
    ]

    operations = [
        migrations.CreateModel(
            name='Pruebamela',
            fields=[
                ('id_cosa', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
            ],
        ),
    ]
