# Generated by Django 4.1.5 on 2023-02-25 00:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='domicilio',
            fields=[
                ('codigo_domicilio', models.BigAutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
                ('colonia', models.CharField(max_length=50)),
                ('numero', models.CharField(max_length=5)),
                ('municipio', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='lole',
            fields=[
                ('codigo_domicilio', models.BigAutoField(primary_key=True, serialize=False)),
                ('calle', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='usuarioXDDD',
            fields=[
                ('nombre', models.CharField(max_length=50)),
                ('codigo_cliente', models.BigAutoField(primary_key=True, serialize=False)),
                ('telefono', models.CharField(max_length=10)),
                ('codigo_domicilio', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='proyectoSBBDDAPP.domicilio')),
            ],
        ),
    ]
