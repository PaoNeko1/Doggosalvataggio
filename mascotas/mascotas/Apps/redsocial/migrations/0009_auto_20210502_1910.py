# Generated by Django 3.2 on 2021-05-02 23:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('redsocial', '0008_alter_pet_foto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usuario',
            name='Edad',
            field=models.IntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='Email',
            field=models.CharField(max_length=80),
        ),
    ]