from django.shortcuts import render
from .models import Consulta, Paciente

def home(request):
    return render(request, 'website/home.html')


def register_view(request):
    if request.method == 'POST':
        # Lógica de cadastro do usuário
        pass
    return render(request, 'website/register.html')
    
def buscar_consultas_por_cpf(cpf_paciente):
    nome_paciente = None
    nome_paciente = Paciente.objects.filter(cpf=cpf_paciente)
    nome_paciente = nome_paciente.first()

    # Usa select_related para otimizar consultas relacionadas
    consultas = Consulta.objects.filter(paciente__cpf=cpf_paciente).select_related(
        'medico', 'medico__cpf', 'atendente', 'atendente__cpf', 'paciente', 'paciente__cpf'
    ).order_by('data_consulta')

    resultados = []
    if consultas.exists():
        for consulta in consultas:
            resultados.append({
                'data_consulta': consulta.data_consulta,
                'especialidade_medico': consulta.medico.especialidade,  # Especialidade do médico
                'nome_medico': consulta.medico.cpf.nome,  # Nome do médico relacionado
                'nome_atendente': consulta.atendente.cpf.nome,  # Nome do atendente relacionado
                'prontuario': consulta.prontuario,
            })

    return nome_paciente, resultados


def consultas_view(request):
    cpf = request.GET.get('cpf', '')
    
    resultados = []
    # resultados é uma lista de dicionários iguais

    nome_paciente = None
    if cpf:
        nome_paciente, resultados = buscar_consultas_por_cpf(cpf)

        # Tratamento da saída
        for resultado in resultados:

            # Data da consulta, deixar em português
            resultado['data_consulta'] = resultado['data_consulta'].strftime('%d/%m/%Y')
            
            # Especialidade, nome do médico e nome do atendente, deixar somente as primeiras letras maiúsculas
            resultado['especialidade_medico'] = resultado['especialidade_medico'].title()
            resultado['nome_medico'] = resultado['nome_medico'].title()
            resultado['nome_atendente'] = resultado['nome_atendente'].title()

            # Prontuario
            if resultado['prontuario'] is None:
                resultado['prontuario'] = "Indisponível"

    return render(request, 'website/consultas.html', {
        'cpf': cpf,
        'nome_paciente': nome_paciente,
        'resultados': resultados
    })
