from django.db import models

class Usuario(models.Model):
    cpf = models.CharField(max_length=11, primary_key=True, db_column='cpf')
    email = models.EmailField(unique=True, db_column='email')
    senha = models.CharField(max_length=20, db_column='senha')
    nome = models.CharField(max_length=75, db_column='nome')
    data_nascimento = models.DateField(db_column='data_nascimento')
    genero = models.CharField(max_length=1, choices=[('M', 'Masculino'), ('F', 'Feminino'), ('N', 'Não Informado')], db_column='genero')
    telefone = models.CharField(max_length=11, db_column='telefone')
    cep = models.CharField(max_length=8, db_column='cep')
    numero = models.CharField(max_length=5, db_column='numero')
    cidade = models.CharField(max_length=30, db_column='cidade')
    estado = models.CharField(max_length=2, db_column='estado')

    class Meta:
        db_table = 'usuarios'

    def __str__(self):
        return self.nome


class Medico(models.Model):
    crm = models.CharField(max_length=10, primary_key=True, db_column='crm')
    cpf = models.OneToOneField(Usuario, on_delete=models.CASCADE, related_name='medico', db_column='cpf')
    especialidade = models.CharField(max_length=50, db_column='especialidade')

    class Meta:
        db_table = 'medicos'

    def __str__(self):
        return f"{self.cpf.nome} ({self.especialidade})"


class Atendente(models.Model):
    cpf = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='atendente', db_column='cpf')
    data_contratacao = models.DateField(db_column='data_contratacao')

    class Meta:
        db_table = 'atendentes'

    def __str__(self):
        return self.cpf.nome


class Paciente(models.Model):
    cpf = models.OneToOneField(Usuario, on_delete=models.CASCADE, primary_key=True, related_name='paciente', db_column='cpf')
    convenio = models.CharField(max_length=30, db_column='convenio')
    altura = models.DecimalField(max_digits=3, decimal_places=2, db_column='altura')
    peso = models.DecimalField(max_digits=4, decimal_places=1, db_column='peso')

    class Meta:
        db_table = 'pacientes'

    def __str__(self):
        return self.cpf.nome


class Alergia(models.Model):
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='alergias', db_column='paciente_cpf')
    alergia = models.CharField(max_length=50, db_column='alergia')

    class Meta:
        db_table = 'alergias'
        unique_together = ('paciente', 'alergia')

    def __str__(self):
        return f"{self.paciente.cpf.nome} - {self.alergia}"


class Consulta(models.Model):
    medico = models.ForeignKey(Medico, on_delete=models.CASCADE, related_name='consultas', db_column='medico_crm')
    paciente = models.ForeignKey(Paciente, on_delete=models.CASCADE, related_name='consultas', db_column='paciente_cpf')
    atendente = models.ForeignKey(Atendente, on_delete=models.CASCADE, related_name='consultas', db_column='atendente_cpf')
    data_consulta = models.DateField(db_column='data_consulta')
    prontuario = models.TextField(null=True, blank=True, db_column='prontuario')

    class Meta:
        db_table = 'consultas'
        unique_together = ('medico', 'paciente', 'atendente', 'data_consulta')

    def __str__(self):
        return f"Consulta em {self.data_consulta} - Paciente: {self.paciente.cpf.nome}"
