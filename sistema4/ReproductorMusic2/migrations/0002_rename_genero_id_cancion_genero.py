# Generated by Django 4.2.4 on 2023-09-05 20:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ReproductorMusic2', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cancion',
            old_name='genero_id',
            new_name='genero',
        ),
    ]