from django.shortcuts import render
from .models import Consulta

def home(request):
    return render(request, 'website/home.html')

# def consultas(request):
#     # Verifica se o usuário está logado
#     if not request.user.is_authenticated:
#         return render(request, 'website/login.html')
#     return render(request, 'website/consultas.html')

def login_view(request):
    # Lógica de login (exemplo simplificado)
    if request.method == 'POST':
        # Autenticação aqui
        pass
    return render(request, 'website/login.html')

def register_view(request):
    if request.method == 'POST':
        # Lógica de cadastro do usuário
        pass
    return render(request, 'website/register.html')
    
def buscar_consultas_por_cpf(cpf_paciente):
    # Usa select_related para otimizar consultas relacionadas
    consultas = Consulta.objects.filter(paciente__cpf=cpf_paciente).select_related(
        'medico', 'medico__cpf', 'atendente', 'atendente__cpf', 'paciente', 'paciente__cpf'
    ).order_by('data_consulta')

    resultados = []
    for consulta in consultas:
        resultados.append({
            'data_consulta': consulta.data_consulta,
            'nome_medico': consulta.medico.cpf.nome,  # Nome do médico relacionado
            'nome_atendente': consulta.atendente.cpf.nome,  # Nome do atendente relacionado
            'prontuario': consulta.prontuario,
        })

    return resultados


def consultas_view(request):
    cpf = request.GET.get('cpf', '')
    resultados = []

    if cpf:
        resultados = buscar_consultas_por_cpf(cpf)

    return render(request, 'website/consultas.html', {'resultados': resultados, 'cpf': cpf})
