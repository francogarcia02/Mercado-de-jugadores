# Generated by Django 2.2 on 2020-12-08 04:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_transaccion_precio'),
    ]

    operations = [
        migrations.AddField(
            model_name='transaccion',
            name='media',
            field=models.IntegerField(default=0),
        ),
    ]
