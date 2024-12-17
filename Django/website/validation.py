from datetime import datetime
import re

# Funções para validação de entrada de dados, retornam falso se a entrada fornecida não estiver no formato especificado

def validar_cpf(cpf):
    """
    Deixa o cpf somente com numéricos e verifica se tem 11 caracteres.
    """
    cpf = re.sub(r"[^\w]", "", cpf)
    if not (len(cpf) == 11 and cpf.isdigit()):
        raise ValueError("CPF inválido: deve conter exatamente 11 números.")

def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
    except ValueError:
        raise ValueError("Data inválida: use o formato YYYY-MM-DD.")

def validar_genero(genero):
    if genero not in ['M', 'F', 'N']:
        raise ValueError("Gênero inválido, tente novamente.")

def validar_telefone(telefone):
    telefone = re.sub(r"[^\w]", "", telefone)
    if not (len(telefone) == 10 or len(telefone) == 11) and telefone.isdigit():
        raise ValueError("Telefone inválido: deve conter 10 ou 11 números.")

def validar_cep(cep):
    cep = re.sub(r"[^\w]", "", cep)
    if not (len(cep) == 8 and cep.isdigit()):
        raise ValueError("CEP inválido: deve conter exatamente 8 números.")

def validar_estado(estado):
    estados = {
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    }
    if estado not in estados:
        raise ValueError("Estado inválido: deve ser uma sigla válida.")

def validar_crm(crm):
    estados = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO',
               'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI',
               'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}
    crm = crm.strip().replace("-", "")
    if not re.fullmatch(r'\d{1,7}[A-Z]{2}', crm):
        raise ValueError("CRM inválido: formato deve conter até 7 dígitos seguidos de uma sigla de estado.")
    sigla = crm[-2:]
    if sigla not in estados:
        raise ValueError("CRM inválido: estado fornecido não é válido.")

def validar_email(email):
    padrao = re.compile(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$')
    if not padrao.match(email):
        raise ValueError("E-mail inválido: verifique o formato.")
    
def validar_senha(senha):
    if len(senha) > 20 or len(senha) < 8:
        raise ValueError("Senha inválida: deve ter entre 8 e 20 caracteres.")
    tem_maiuscula = re.search(r'[A-Z]', senha)
    tem_minuscula = re.search(r'[a-z]', senha)
    tem_numero = re.search(r'\d', senha)
    tem_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)

    if not (tem_maiuscula and tem_minuscula and tem_numero and tem_especial):
        raise ValueError("Senha inválida: deve conter ao menos uma letra maiúscula, uma minúscula, um número e um caractere especial.")

def validar_altura(altura):
    if altura <= 0 or altura >= 10:
        raise ValueError("Altura inválida: deve estar entre 0 e 10 metros.")
    return round(altura, 2)

def validar_peso(peso):
    if peso <= 0 or peso >= 1000:
        raise ValueError("Peso inválido: deve estar entre 0 e 1000 kg.")
    return round(peso, 1)