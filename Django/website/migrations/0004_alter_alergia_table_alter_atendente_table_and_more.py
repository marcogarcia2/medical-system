# Generated by Django 5.1.4 on 2024-12-12 15:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0003_alter_alergia_table_alter_atendente_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='alergia',
            table='website_alergias',
        ),
        migrations.AlterModelTable(
            name='atendente',
            table='website_atendentes',
        ),
        migrations.AlterModelTable(
            name='medico',
            table='website_medicos',
        ),
        migrations.AlterModelTable(
            name='paciente',
            table='website_pacientes',
        ),
        migrations.AlterModelTable(
            name='usuario',
            table='website_usuarios',
        ),
    ]