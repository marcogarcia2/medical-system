# Generated by Django 5.1.4 on 2024-12-12 15:04

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_alter_usuario_table'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='alergia',
            table='alergias',
        ),
        migrations.AlterModelTable(
            name='atendente',
            table='atendentes',
        ),
        migrations.AlterModelTable(
            name='medico',
            table='medicos',
        ),
        migrations.AlterModelTable(
            name='paciente',
            table='pacientes',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='usuarios',
        ),
    ]