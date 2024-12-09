'''
-- Leonardo Gueno Rissetto (13676482)
-- Lucas Lima Romero (13676325)
-- Luciano Gonçalves Lopes Filho (13676520)
-- Marco Antonio Gaspar Garcia (11833581)
-- Thiago Kashivagui Gonçalves (13676579)
'''

import psycopg2
import os
from psycopg2 import sql
from datetime import datetime
import re  # Biblioteca para expressões regulares
import colorful as cf # Biblioteca que imprime texto com cores

# Função para conectar ao banco usando variáveis de ambiente
def connect_db():
    try:
        conn = psycopg2.connect(
            dbname=os.getenv("DB_NAME"),
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=os.getenv("DB_PORT")
        )
        return conn
    except Exception as e:
        print(f"Erro ao conectar ao banco: {e}")
        exit()
# -------------------------------------------------------------------------- #

# Funções para validação de entrada de dados, retornam falso se a entrada fornecida não estiver no formato especificado
def validar_cpf(cpf):
    """
    Deixa o cpf somente com alfanuméricos e verifica se tem 11 caracteres.
    """
    cpf = re.sub(r"[^\w]", "", cpf)
    if len(cpf) == 11 and cpf.isdigit():
        return True, cpf
    return False, cpf

def validar_data(data):
    try:
        datetime.strptime(data, "%Y-%m-%d")
        return True
    except ValueError:
        return False

def validar_genero(genero):
    return genero.upper() in ["M", "F", "N"]  # M: Masculino, F: Feminino, N: Não especificado

def validar_telefone(telefone):
    telefone = re.sub(r"[^\w]", "", telefone)
    if (len(telefone) == 10 or len(telefone) == 11) and telefone.isdigit():
        return True, telefone
    return False, telefone

def validar_cep(cep):
    cep = re.sub(r"[^\w]", "", cep)
    if len(cep) == 8 and cep.isdigit():
        return True, cep
    return False, cep

def validar_estado(estado):
    estados = {
    'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
    'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
    'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'
    }
    return estado if estado in estados else None

def validar_crm(crm):
    """
    Valida um número de CRM.
    Regras:
    - Até 7 dígitos seguidos de 2 letras representando estados brasileiros.
    - Aceita hífen opcional (que será removido).
    - Retorna False se for inválido.
    - Retorna o CRM normalizado se for válido (números e letras, sem hífen).
    
    :param crm: str - O CRM a ser validado.
    :return: str|bool - CRM normalizado se válido, False caso contrário.
    """
    # Lista de siglas de estados brasileiros
    estados = {'AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 
               'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 
               'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'}

    # Remover espaços extras e hífen
    crm = crm.strip().replace("-", "")

    # Expressão regular para validar formato: até 7 dígitos seguidos de 2 letras
    if re.fullmatch(r'\d{1,7}[A-Z]{2}', crm):
        # Separar a sigla e verificar se é válida
        sigla = crm[-2:]
        if sigla in estados:
            return True, crm  # Retorna o CRM normalizado (sem hífen)

    return False, crm  # Retorna False se for inválido

def validar_email(email):
    """
    Verifica se a string fornecida é um e-mail válido em qualquer formato válido globalmente.
    
    :param email: str - O e-mail a ser validado.
    :return: tuple - (True, email) se válido, ou (False, None) caso contrário.
    """
    # Expressão regular para validar formatos amplos de e-mails
    padrao = re.compile(
        r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    )
    
    # Verifica se o e-mail corresponde ao padrão
    if padrao.match(email):
        return email
    else:
        return None
    
def validar_senha(senha):
    """
    Valida uma senha conforme as regras:
    - Máximo de 20 caracteres.
    - Pelo menos uma letra maiúscula.
    - Pelo menos uma letra minúscula.
    - Pelo menos um número.
    - Pelo menos um caractere especial.
    
    :param senha: str - A senha a ser validada.
    :return: bool - True se a senha for válida, False caso contrário.
    """
    # Verifica o comprimento da senha
    if len(senha) > 20 or len(senha) < 8:
        return None
    
    # Regex para verificar os critérios
    tem_maiuscula = re.search(r'[A-Z]', senha)
    tem_minuscula = re.search(r'[a-z]', senha)
    tem_numero = re.search(r'\d', senha)
    tem_especial = re.search(r'[!@#$%^&*(),.?":{}|<>]', senha)

    # Verifica se todos os critérios são atendidos
    if tem_maiuscula and tem_minuscula and tem_numero and tem_especial:
        return senha
    else:
        return None

def validar_altura(altura):
    if altura <= 0 or altura >= 10:
        return False, altura
    return True, round(altura, 2)

def validar_peso(peso):
    if peso <=0 or peso >= 1000:
        return False, peso
    return True, round(peso, 1)
# -------------------------------------------------------------------------- #

# Função para cadastrar usuários no sistema
def cadastrar_usuario(conn):
    print(cf.bold("\nInsira os dados do Usuário"))
    try:

        # Solicita e valida os dados do usuário, cada campo de uma vez

        # CPF
        while True:
            cpf = input(cf.bold("CPF do Usuário (somente números): ")).strip()
            ret, cpf = validar_cpf(cpf)
            if ret:
                break
            print(cf.red("CPF inválido! Tente novamente."))

        # Email
        while True:
            email = input(cf.bold("Email: ")).strip()
            email = validar_email(email)
            if email is not None:
                break
            print(cf.red("Email inválido! Tente novamente."))
        
        # Senha
        while True:
            senha = input(cf.bold("Senha: ")).strip()
            senha = validar_senha(senha)
            if senha is not None:
                copia = input(cf.bold("Repita a senha: ")).strip()
                if copia == senha:
                    break
                print(cf.bold_red("As senhas não coincidem."))

            print(cf.red("Senha inválida!"))
            print("Sua senha precisa ter pelo menos uma letra maiúscula, uma letra minúscula, um número e um caractere especial.")
            print("Além disso, deve ter entre 8 e 20 dígitos.")

        # Nome
        while True:
            nome = input(cf.bold("Nome: ")).strip().upper()
            if len(nome) <= 75 and len(nome) >= 0:
                break
            print(cf.red("Nome muito grande!"))

        # Data de Nascimento
        while True:
            try:
                data_nascimento = input(cf.bold("Data de Nascimento (DD-MM-YYYY): ")).strip()
                data_nascimento = datetime.strptime(data_nascimento, "%d-%m-%Y").strftime("%Y-%m-%d")
                if validar_data(data_nascimento):
                    break
            except Exception as e:
                print(cf.red("Data inválida! Tente novamente."))

        # Gênero
        while True:
            genero = input(cf.bold("Gênero(M/F): ")).strip().upper()
            if validar_genero(genero):
                break
            print(cf.red("Gênero inválido! Use M, F ou N."))

        # Telefone
        while True:
            telefone = input(cf.bold("Telefone: ")).strip()
            ret, telefone = validar_telefone(telefone)
            if ret:
                break
            print(cf.red("Telefone inválido! Tente novamente."))

        # CEP
        while True:
            cep = input(cf.bold("CEP: ")).strip()
            ret, cep = validar_cep(cep)
            if ret:
                break
            print(cf.red("CEP inválido! Tente novamente."))
        
        # Número
        while True:
            numero = input(cf.bold("Número: ")).strip()
            if numero.isdigit() and len(numero) <= 5 and len(numero) >= 0:
                break
            print(cf.red("Número inválido! Tente novamente."))
        
        # Cidade
        cidade = input(cf.bold("Cidade: ")).strip().upper()
        
        # Estado
        while True:
            estado = input(cf.bold("Estado (sigla): ")).strip().upper()
            estado = validar_estado(estado)
            if estado is not None:
                break
            print(cf.red("Estado inválido! Tente novamente."))

        # Realiza a inserção, depois de todos os dados validados
        with conn.cursor() as cur:
            query = sql.SQL("""
                INSERT INTO Usuarios (cpf, email, senha, nome, data_nascimento, genero, telefone, cep, numero, cidade, estado)
                VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
            """)
            cur.execute(query, (cpf, email, senha, nome, data_nascimento, genero, telefone, cep, numero, cidade, estado))
            conn.commit()    

        # Se não houve erro, o usuário foi inserido com sucesso no BD
        print(cf.bold_green("\nUsuário cadastrado com sucesso!\n"))

        # Agora pergunta quem está usando o sistema
        cadastrar_especializacao(conn, cpf)
    
    # Caso ocorram erros, aqui há o tratamento sem finalizar a aplicação
    except psycopg2.Error as e:
        print(cf.bold_red("Erro ao cadastrar usuário no banco: ") + cf.red(f"{e}"))
        conn.rollback()

    except Exception as e:
        print(cf.red(f"Erro inesperado: {e}"))

# Função que, dado um usuário, define sua especialização no sistema e insere no banco
def cadastrar_especializacao(conn, cpf):

    while True:
    # Selecionar a especialização do usuário em si
        print(cf.bold_yellow("Nos diga quem é você: "))
        print(cf.bold("1. ") + "Médico")
        print(cf.bold("2. ") + "Atendente")
        print(cf.bold("3. ") + "Paciente")
        print(cf.bold("4. ") + "Nenhum\n")
        spec = input(cf.bold("Escolha uma opção: ")).strip()

        # Médico
        if spec == "1":
            cadastrar_medico(conn, cpf)
            break
        elif spec == "2":
            cadastrar_atendente(conn, cpf)
            break
        elif spec == "3":
            cadastrar_paciente(conn, cpf)
            break
        elif spec == "4":
            break
        else:
            print(cf.bold_red("Opção Inválida! Tente Novamente.\n"))

# Função que cadastra um médico no banco, dado um CPF
def cadastrar_medico(conn, cpf):
    try:
        # CRM
        while True:
            crm = input(cf.bold("Informe seu CRM: ")).strip().upper()
            ret, crm = validar_crm(crm)
            if ret:
                break
            print(cf.red("CRM inválido! Tente novamente."))

        # Especialidade
        while True:
            especialidade = input(cf.bold("Especialidade (ex. Ortopedista): ")).strip().upper()
            if len(especialidade) <= 50 and len(especialidade) >= 0:
                break
            print(cf.red("Nome de especialidade muito grande! Tente novamente."))
    
        # Insere os dados validados no banco
        with conn.cursor() as cur:
            query = sql.SQL("""
                INSERT INTO Medicos (crm, cpf, especialidade)
                VALUES (%s, %s, %s)
            """)
            cur.execute(query, (crm, cpf, especialidade))
            conn.commit()
            print(cf.bold_green("\nMédico cadastrado com sucesso!"))

    # Tratamento de erros
    except psycopg2.Error as e:
        print(cf.bold_red("Erro ao cadastrar médico no banco: ") + cf.red(f"{e}"))
        conn.rollback()

    except Exception as e:
        print(cf.red(f"Erro inesperado: {e}"))

# Função que cadastra um atendente no banco, dado um CPF
def cadastrar_atendente(conn, cpf):
    try:
        
        # Data de Contratação
        while True:
            try:
                data_contratacao = input(cf.bold("Informe sua Data de Contratação (DD-MM-YYYY): ")).strip()
                data_contratacao = datetime.strptime(data_contratacao, "%d-%m-%Y").strftime("%Y-%m-%d")
                if validar_data(data_contratacao):
                    break
            except Exception as e:
                print(cf.red("Data inválida! Tente novamente."))
    
        # Insere os dados validados no banco
        with conn.cursor() as cur:
            query = sql.SQL("""
                INSERT INTO Atendentes (cpf, data_contratacao)
                VALUES (%s, %s)
            """)
            cur.execute(query, (cpf, data_contratacao))
            conn.commit()

    # Tratamento de erros
    except psycopg2.Error as e:
        print(cf.bold_red("Erro ao cadastrar atendente no banco: ") + cf.red(f"{e}"))
        conn.rollback()

    except Exception as e:
        print(cf.red(f"Erro inesperado: {e}"))

# Função que cadastra um paciente no banco, dado um CPF
def cadastrar_paciente(conn, cpf):
    try:
        # Convênio
        while True:
            convenio = input(cf.bold("Convênio: ")).strip().upper()
            if len(convenio) <= 30 and len(convenio) >= 0:
                break
            print(cf.red("Nome do convênio muito grande!"))

        # Altura
        while True:
            try:
                altura = float(input(cf.bold("Altura (em metros, ex: 1.80): ")).strip())
                ret, altura = validar_altura(altura)
                if ret:
                    break
            except ValueError:
                pass
            print(cf.red("Altura inválida! Tente novamente."))

        # Peso
        while True:
            try:
                peso = float(input(cf.bold("Peso (em kg, ex: 70.5): ")).strip())
                ret, peso = validar_peso(peso)
                if ret:
                    break
            except ValueError:
                pass
            print(cf.red("Peso inválido! Tente novamente."))
    
        # Insere os dados validados no banco
        with conn.cursor() as cur:
            query = sql.SQL("""
                INSERT INTO Pacientes (cpf, convenio, altura, peso)
                VALUES (%s, %s, %s, %s)
            """)
            cur.execute(query, (cpf, convenio, altura, peso))
            conn.commit()

    # Tratamento de erros
    except psycopg2.Error as e:
        print(cf.bold_red("Erro ao cadastrar paciente no banco: ") + cf.red(f"{e}"))
        conn.rollback()

    except Exception as e:
        print(cf.red(f"Erro inesperado: {e}"))  



# Função para consultar jogador
def consultar_historico(conn):

    # Consulta por CPF
    try:
        print(cf.bold("Informe o CPF do paciente que deseja consultar (somente números):"))
        cpf = input(cf.bold_green("--> ")).strip()
        ret, cpf = validar_cpf(cpf)
        if not ret:
            print(cf.red("CPF inválido! Tente novamente."))
            return

        # Realiza a consulta
        with conn.cursor() as cur:
            query = sql.SQL("""
                SELECT 
                    c.data_consulta AS DataConsulta,
                    u_med.nome AS NomeMedico,
                    u_at.nome AS NomeAtendente,
                    c.prontuario AS Prontuario
                FROM 
                    Consultas c
                INNER JOIN 
                    Medicos m ON c.medico_crm = m.crm
                INNER JOIN 
                    Usuarios u_med ON m.cpf = u_med.cpf
                INNER JOIN 
                    Atendentes a ON c.atendente_cpf = a.cpf
                INNER JOIN 
                    Usuarios u_at ON a.cpf = u_at.cpf
                WHERE 
                    c.paciente_cpf = %s
                ORDER BY 
                    c.data_consulta ASC;
            """)
            cur.execute(query, (cpf,))
            consultas = cur.fetchall()

        # Se encontrou consultas no sistema, vamos exibir seus dados
        if consultas:

            print(cf.bold((f"\n{'DATA':<20} {'MÉDICO':<30} {'ATENDENTE':<30} {'PRONTUÁRIO':<35}")))
            for consulta in consultas:
                data_c = consulta[0]
                medico = consulta[1]
                atendente = consulta[2]
                prontuario = cf.cyan(consulta[3]) if consulta[3] else cf.red("Indisponível")

                linha = "{:<20}{:<30}{:<30}{:<35}".format(str(data_c), medico.title(), atendente.title(), prontuario)
                print(linha)

        else:
            print(cf.bold_red("\nNenhuma consulta encontrada para este paciente."))

    except psycopg2.Error as e:
        print(cf.bold_red("Erro ao consultar dados no banco: ") + cf.red(f"{e}"))
    
    except Exception as e:
        print(cf.red("Erro:") + f"{e}")

# Menu principal
def menu():

    conn = None

    # Conecta com o BD, e oferece as opções para o usuário
    try:
        conn = connect_db()

        while True:
            print(cf.bold_yellow("\nSistema de Gerenciamento de Consultas Médicas"))
            print(cf.bold("1.") + " Cadastrar Usuário")
            print(cf.bold("2.") + " Consultar Histórico de Consultas")
            print(cf.bold("3.") + " Definir Papel do Usuário no Sistema")
            print(cf.bold("4.") + " Sair\n")

            opcao = input(cf.bold("Escolha uma opção: ")).strip()
            if opcao == "1":
                cadastrar_usuario(conn)

            elif opcao == "2":
                consultar_historico(conn)

            elif opcao == "3":
                while True:
                    cpf = input(cf.bold("CPF do Usuário (somente números): ")).strip()
                    ret, cpf = validar_cpf(cpf)
                    if ret:
                        break
                    print(cf.red("CPF inválido! Tente novamente."))
                cadastrar_especializacao(conn, cpf)        

            elif opcao == "4":
                print(cf.bold("\nSaindo..."))
                break

            else:
                print(cf.bold("Opção inválida! Tente novamente."))

    # Caso o usuário saia com Ctrl+C, exibir uma saída mais elegante
    except KeyboardInterrupt as e:
        print(cf.bold("\n\nSaindo..."))

    finally:
        # Fechar conexão
        conn.close()

# Executa o sistema
if __name__ == "__main__":
    menu()
