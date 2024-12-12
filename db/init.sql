-- Leonardo Gueno Rissetto (13676482)
-- Lucas Lima Romero (13676325)
-- Luciano Gonçalves Lopes Filho (13676520)
-- Marco Antonio Gaspar Garcia (11833581)
-- Thiago Kashivagui Gonçalves (13676579)

-- Script de inicialização da Base de Dados do Sistema de Gerenciamento de Consultas Médicas

-- Tabela que guardará informações sobre todos os usuários do sistema
CREATE TABLE Usuarios (

    -- Atributos do usuário do sistema
    cpf CHAR(11) NOT NULL,
    email VARCHAR(50) NOT NULL,
    senha VARCHAR(20) NOT NULL,
    nome VARCHAR(75) NOT NULL,
    data_nascimento DATE NOT NULL,
    genero CHAR(1) NOT NULL,
    telefone VARCHAR(11) NOT NULL,
    cep CHAR(8) NOT NULL,
    numero VARCHAR(5) NOT NULL,
    cidade VARCHAR(30) NOT NULL,
    estado CHAR(2) NOT NULL,

    -- Constraints de Usuarios, para manter a consistência
    CONSTRAINT pk_usuario PRIMARY KEY (cpf),
    CONSTRAINT uni_usuario UNIQUE (email),
    CONSTRAINT ck_usuario_1 CHECK (genero in ('M', 'F', 'N')),
    CONSTRAINT ck_usuario_2 CHECK (cpf ~ '^\d{11}$'),
    CONSTRAINT ck_usuario_3 CHECK (cep ~ '^\d{8}$'),
    CONSTRAINT ck_usuario_4 CHECK (estado IN ('AC', 'AL', 'AP', 'AM', 'BA', 'CE', 'DF', 'ES', 'GO', 'MA', 'MT', 'MS', 'MG', 'PA', 'PB', 'PR', 'PE', 'PI', 'RJ', 'RN', 'RS', 'RO', 'RR', 'SC', 'SP', 'SE', 'TO'))
);

-- Tabela que guardará informações sobre os médicos
CREATE TABLE Medicos (

    -- Atributos de médico
    crm VARCHAR(10) NOT NULL,
    cpf CHAR(11) NOT NULL,
    especialidade VARCHAR(50) NOT NULL,

    -- Constraints de médicos 
    CONSTRAINT pk_medico PRIMARY KEY (crm),
    CONSTRAINT uni_medico UNIQUE(cpf),
    CONSTRAINT fk_medico FOREIGN KEY (cpf) REFERENCES Usuarios (cpf) ON DELETE CASCADE
);

-- Tabela dos atendentes, funcionários que marcam consultas
CREATE TABLE Atendentes (

    -- Atributos de atendentes
    cpf CHAR(11) NOT NULL,
    data_contratacao DATE NOT NULL,
    
    -- Constraints de Atendentes
    CONSTRAINT pk_atendentes PRIMARY KEY (cpf),
    CONSTRAINT fk_atendentes FOREIGN KEY (cpf) REFERENCES Usuarios (cpf) ON DELETE CASCADE
);

-- Tabela de pacientes
CREATE TABLE Pacientes (

    -- Atributos de paciente
    cpf CHAR(11) NOT NULL,
    convenio VARCHAR(30) NOT NULL,
    altura DECIMAL(3,2) NOT NULL,
    peso DECIMAL(4,1) NOT NULL,

    -- Constraints de paciente
    CONSTRAINT pk_pacientes PRIMARY KEY (cpf),
    CONSTRAINT fk_pacientes FOREIGN KEY (cpf) REFERENCES Usuarios (cpf) ON DELETE CASCADE
);

-- Tabela que guardará alergias de cada paciente
CREATE TABLE Alergias (

    -- Atributos
    paciente_cpf CHAR(11) NOT NULL,
    alergia VARCHAR(50) NOT NULL,

    -- Constraints de alergias
    CONSTRAINT pk_alergias PRIMARY KEY (paciente_cpf, alergia),
    CONSTRAINT fk_alergias FOREIGN KEY (paciente_cpf) REFERENCES Pacientes (cpf) ON DELETE CASCADE
);

-- Consultas, envolvem um médico, um paciente e um atendente
CREATE TABLE Consultas (

    -- Atributos de consulta
    id SERIAL NOT NULL,
    medico_crm VARCHAR(10) NOT NULL,
    paciente_cpf CHAR(11) NOT NULL,
    atendente_cpf CHAR(11) NOT NULL,
    data_consulta DATE NOT NULL,
    prontuario VARCHAR(50),

    -- Constraints de consulta
    CONSTRAINT pk_consultas PRIMARY KEY (id),
    CONSTRAINT uni_consultas_1 UNIQUE (medico_crm, paciente_cpf, atendente_cpf, data_consulta),
    CONSTRAINT uni_consultas_2 UNIQUE (prontuario),
    CONSTRAINT fk_consultas_1 FOREIGN KEY (medico_crm) REFERENCES Medicos (crm) ON DELETE CASCADE,
    CONSTRAINT fk_consultas_2 FOREIGN KEY (paciente_cpf) REFERENCES Pacientes (cpf) ON DELETE CASCADE,
    CONSTRAINT fk_consultas_3 FOREIGN KEY (atendente_cpf) REFERENCES Atendentes (cpf) ON DELETE CASCADE
);

