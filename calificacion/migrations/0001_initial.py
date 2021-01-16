# Generated by Django 2.2.12 on 2021-01-16 00:59

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Carrera',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=150, verbose_name='Título')),
                ('duracion_carrera', models.FloatField()),
                ('descripcion', models.TextField(help_text='Descripción corta')),
                ('imagen', models.ImageField(upload_to='img/')),
                ('video', models.FileField(null=True, upload_to='videos/', verbose_name='')),
                ('semestre', models.IntegerField(choices=[(1, 'primero'), (2, 'segundo'), (3, 'tercero'), (4, 'cuarto'), (5, 'quinto'), (6, 'sexto'), (7, 'septimo'), (8, 'optavo'), (9, 'noveno')], default=1)),
            ],
            options={
                'ordering': ['titulo'],
            },
        ),
        migrations.CreateModel(
            name='Materia',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=200)),
                ('parcial_1', models.FloatField(default=0)),
                ('parcial_2', models.FloatField(default=0)),
                ('parcial_3', models.FloatField(default=0)),
                ('maestro_asignado', models.CharField(max_length=200)),
                ('carrera', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='calificacion.Carrera')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]