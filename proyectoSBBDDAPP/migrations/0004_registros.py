# Generated by Django 4.1.5 on 2023-03-02 21:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectoSBBDDAPP', '0003_tecnico_reporte'),
    ]

    operations = [
        migrations.CreateModel(
            name='registros',
            fields=[
                ('id_consulta', models.BigAutoField(primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField()),
                ('folio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyectoSBBDDAPP.reporte')),
            ],
        ),
    ]
