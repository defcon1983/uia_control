# Generated by Django 2.2.12 on 2021-01-16 03:28

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('calificacion', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='materia',
            name='carrera',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='calificacion.Carrera'),
        ),
    ]
