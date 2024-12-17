from django import forms
from django.shortcuts import render, redirect
from .models import Usuario, Consulta, Paciente, Medico, Atendente
from django.db import IntegrityError
from django.contrib import messages
from .validation import *

def home(request):
    return render(request, 'website/home.html')


class RegistroForm(forms.ModelForm):
    class Meta:
        model = Usuario
        fields = ['cpf', 'email', 'senha', 'nome', 'data_nascimento', 'genero', 'telefone', 'cep', 'numero', 'cidade', 'estado']
        widgets = {
            'senha': forms.PasswordInput(),  # Mostra o campo como senha
        }

# 
def register_view(request):
    # Funções para validação dos dados

    if request.method == 'POST':
        try:
            # Captura os dados do formulário e valida
            cpf = request.POST['cpf']
            validar_cpf(cpf)

            email = request.POST['email']
            validar_email(email)

            senha = request.POST['senha']
            #validar_senha(senha)

            nome = request.POST['nome'].upper()
            
            data_nascimento = request.POST['data_nascimento']
            validar_data(data_nascimento)

            genero = request.POST['genero'].upper()
            validar_genero(genero)

            telefone = request.POST['telefone']
            validar_telefone(telefone)

            cep = request.POST['cep']
            validar_cep(cep)
            
            numero = request.POST['numero'].upper()

            cidade = request.POST['cidade'].upper()
            
            estado = request.POST['estado'].upper()
            validar_estado(estado)
            
            # Criação do usuário
            usuario = Usuario.objects.create(
                cpf=cpf,
                email=email,
                senha=senha,
                nome=nome,
                data_nascimento=data_nascimento,
                genero=genero,
                telefone=telefone,
                cep=cep,
                numero=numero,
                cidade=cidade,
                estado=estado
            )

            print(usuario, flush=True)
            
            # Verifica o tipo de usuário
            tipo_usuario = request.POST['tipo_usuario']
            if tipo_usuario == 'medico':
                
                crm = request.POST['crm']
                validar_crm(crm)

                especialidade=request.POST['especialidade']

                Medico.objects.create(
                    cpf=usuario,
                    crm=crm,
                    especialidade=especialidade
                )

            elif tipo_usuario == 'paciente':
                
                convenio = request.POST['convenio'].upper()
                altura = float(request.POST['altura'])
                altura = validar_altura(altura)
                peso = float(request.POST['peso'])
                peso = validar_peso(peso)

                Paciente.objects.create(
                    cpf=usuario,
                    convenio=convenio,
                    altura=altura,
                    peso=peso
                )

            elif tipo_usuario == 'atendente':

                data_contratacao = request.POST['data_contratacao']
                validar_data(data_contratacao)

                Atendente.objects.create(
                    cpf=usuario,
                    data_contratacao=data_contratacao
                )
    
            messages.success(request, "Usuário cadastrado com sucesso!")
            return redirect('/')  # Redireciona para a página inicial

        except IntegrityError as e:
            # Identifica qual constraint foi violada
            if 'pk_usuario' in str(e):  
                messages.error(request, "Erro: CPF já está cadastrado.")
            elif 'uni_usuario' in str(e):  # Nome da constraint UNIQUE para email
                messages.error(request, "Erro: Este email já está em uso.")
            else:
                messages.error(request, "Erro de integridade: Verifique os dados fornecidos.")

        except Exception as e:
            messages.error(request, f"Erro inesperado: {str(e)}")

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
