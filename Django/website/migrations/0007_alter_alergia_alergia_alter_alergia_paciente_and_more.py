# Generated by Django 5.1.4 on 2024-12-12 15:48

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0006_rename_alergias_alergia_rename_atendentes_atendente_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='alergia',
            name='alergia',
            field=models.CharField(db_column='alergia', max_length=50),
        ),
        migrations.AlterField(
            model_name='alergia',
            name='paciente',
            field=models.ForeignKey(db_column='paciente_cpf', on_delete=django.db.models.deletion.CASCADE, related_name='alergias', to='website.paciente'),
        ),
        migrations.AlterField(
            model_name='atendente',
            name='cpf',
            field=models.OneToOneField(db_column='cpf', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='atendente', serialize=False, to='website.usuario'),
        ),
        migrations.AlterField(
            model_name='atendente',
            name='data_contratacao',
            field=models.DateField(db_column='data_contratacao'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='atendente',
            field=models.ForeignKey(db_column='atendente_cpf', on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='website.atendente'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='data_consulta',
            field=models.DateField(db_column='data_consulta'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='medico',
            field=models.ForeignKey(db_column='medico_crm', on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='website.medico'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='paciente',
            field=models.ForeignKey(db_column='paciente_cpf', on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='website.paciente'),
        ),
        migrations.AlterField(
            model_name='consulta',
            name='prontuario',
            field=models.TextField(blank=True, db_column='prontuario', null=True),
        ),
        migrations.AlterField(
            model_name='medico',
            name='cpf',
            field=models.OneToOneField(db_column='cpf', on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='website.usuario'),
        ),
        migrations.AlterField(
            model_name='medico',
            name='crm',
            field=models.CharField(db_column='crm', max_length=10, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='medico',
            name='especialidade',
            field=models.CharField(db_column='especialidade', max_length=50),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='altura',
            field=models.DecimalField(db_column='altura', decimal_places=2, max_digits=3),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='convenio',
            field=models.CharField(db_column='convenio', max_length=30),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='cpf',
            field=models.OneToOneField(db_column='cpf', on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='paciente', serialize=False, to='website.usuario'),
        ),
        migrations.AlterField(
            model_name='paciente',
            name='peso',
            field=models.DecimalField(db_column='peso', decimal_places=1, max_digits=4),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cep',
            field=models.CharField(db_column='cep', max_length=8),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cidade',
            field=models.CharField(db_column='cidade', max_length=30),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='cpf',
            field=models.CharField(db_column='cpf', max_length=11, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='data_nascimento',
            field=models.DateField(db_column='data_nascimento'),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='email',
            field=models.EmailField(db_column='email', max_length=254, unique=True),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='estado',
            field=models.CharField(db_column='estado', max_length=2),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='genero',
            field=models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não Informado')], db_column='genero', max_length=1),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='nome',
            field=models.CharField(db_column='nome', max_length=75),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='numero',
            field=models.CharField(db_column='numero', max_length=5),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='senha',
            field=models.CharField(db_column='senha', max_length=20),
        ),
        migrations.AlterField(
            model_name='usuario',
            name='telefone',
            field=models.CharField(db_column='telefone', max_length=11),
        ),
    ]
