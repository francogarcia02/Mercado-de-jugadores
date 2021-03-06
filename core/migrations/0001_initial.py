# Generated by Django 2.2 on 2020-12-03 03:34

from django.conf import settings
import django.contrib.auth.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0011_update_proxy_permissions'),
    ]

    operations = [
        migrations.CreateModel(
            name='Club',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('club', models.CharField(max_length=50)),
                ('historia', models.CharField(max_length=50)),
                ('titulos', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='CustomUser',
            fields=[
                ('user_ptr', models.OneToOneField(auto_created=True, on_delete=django.db.models.deletion.CASCADE, parent_link=True, primary_key=True, serialize=False, to=settings.AUTH_USER_MODEL)),
                ('direccion', models.CharField(default=0, max_length=100, verbose_name='Direccion')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
                'abstract': False,
            },
            bases=('auth.user',),
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Imagen',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Jugador',
            fields=[
                ('id', models.IntegerField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('posicion', models.CharField(blank=True, choices=[('Delantero', 'Delantero'), ('Mediocampo', 'Mediocampo'), ('Defenzor', 'Defenzor'), ('Arquero', 'Arquero')], max_length=50)),
                ('edad', models.IntegerField(default=0)),
                ('valor', models.IntegerField(default=0)),
                ('media', models.IntegerField(default=0)),
                ('mediaritmo', models.IntegerField(default=0)),
                ('mediapases', models.IntegerField(default=0)),
                ('mediatiros', models.IntegerField(default=0)),
                ('mediaregates', models.IntegerField(default=0)),
                ('mediadefenza', models.IntegerField(default=0)),
                ('mediafisico', models.IntegerField(default=0)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
            ],
            options={
                'verbose_name': 'Jugador',
                'verbose_name_plural': 'Jugadores',
            },
        ),
        migrations.CreateModel(
            name='Noticia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('epigrafe', models.CharField(max_length=100)),
                ('titular', models.CharField(max_length=100)),
                ('subtitulo', models.CharField(max_length=100)),
                ('entradilla', models.CharField(max_length=300)),
                ('cuerpo', models.CharField(max_length=2000)),
            ],
        ),
        migrations.CreateModel(
            name='Transaccion',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_on', models.DateTimeField(auto_now_add=True)),
                ('customuser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.CustomUser')),
                ('jugador', models.ForeignKey(on_delete='nombre', to='core.Jugador')),
            ],
        ),
        migrations.CreateModel(
            name='Propios',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jugador', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Jugador')),
            ],
            options={
                'verbose_name': 'Propio',
                'verbose_name_plural': 'propios',
            },
        ),
        migrations.CreateModel(
            name='DT',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('historia', models.CharField(default='NULL', max_length=60)),
                ('nombre', models.CharField(max_length=50)),
                ('valor', models.CharField(default='1', max_length=50)),
                ('edad', models.CharField(default='1', max_length=50)),
                ('club', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='core.Club')),
            ],
            options={
                'verbose_name': 'Director Tecnico',
                'verbose_name_plural': 'Directores Tecnicos',
            },
        ),
    ]
