# Generated by Django 5.1.4 on 2024-12-11 21:27

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('cpf', models.CharField(max_length=11, primary_key=True, serialize=False)),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('senha', models.CharField(max_length=20)),
                ('nome', models.CharField(max_length=75)),
                ('data_nascimento', models.DateField()),
                ('genero', models.CharField(choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não Informado')], max_length=1)),
                ('telefone', models.CharField(max_length=11)),
                ('cep', models.CharField(max_length=8)),
                ('numero', models.CharField(max_length=5)),
                ('cidade', models.CharField(max_length=30)),
                ('estado', models.CharField(max_length=2)),
            ],
        ),
        migrations.CreateModel(
            name='Atendente',
            fields=[
                ('cpf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='atendente', serialize=False, to='website.usuario')),
                ('data_contratacao', models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name='Paciente',
            fields=[
                ('cpf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, primary_key=True, related_name='paciente', serialize=False, to='website.usuario')),
                ('convenio', models.CharField(max_length=30)),
                ('altura', models.DecimalField(decimal_places=2, max_digits=3)),
                ('peso', models.DecimalField(decimal_places=1, max_digits=4)),
            ],
        ),
        migrations.CreateModel(
            name='Medico',
            fields=[
                ('crm', models.CharField(max_length=10, primary_key=True, serialize=False)),
                ('especialidade', models.CharField(max_length=50)),
                ('cpf', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='medico', to='website.usuario')),
            ],
        ),
        migrations.CreateModel(
            name='Consulta',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('data_consulta', models.DateField()),
                ('prontuario', models.TextField(blank=True, null=True)),
                ('medico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='website.medico')),
                ('atendente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='website.atendente')),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='consultas', to='website.paciente')),
            ],
            options={
                'unique_together': {('medico', 'paciente', 'atendente', 'data_consulta')},
            },
        ),
        migrations.CreateModel(
            name='Alergia',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('alergia', models.CharField(max_length=50)),
                ('paciente', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='alergias', to='website.paciente')),
            ],
            options={
                'unique_together': {('paciente', 'alergia')},
            },
        ),
    ]
