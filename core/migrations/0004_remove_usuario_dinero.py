# Generated by Django 2.2 on 2020-11-25 21:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201125_2133'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='usuario',
            name='dinero',
        ),
    ]
