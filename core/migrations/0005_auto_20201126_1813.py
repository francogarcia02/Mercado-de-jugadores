# Generated by Django 2.2 on 2020-11-26 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0004_remove_usuario_dinero'),
    ]

    operations = [
        migrations.CreateModel(
            name='Dinero',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.RemoveField(
            model_name='propios',
            name='usuario',
        ),
        migrations.DeleteModel(
            name='Usuario',
        ),
    ]