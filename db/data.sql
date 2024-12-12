-- Leonardo Gueno Rissetto (13676482)
-- Lucas Lima Romero (13676325)
-- Luciano Gonçalves Lopes Filho (13676520)
-- Marco Antonio Gaspar Garcia (11833581)
-- Thiago Kashivagui Gonçalves (13676579)

-- Script de alimentação do BD com dados fictícios

INSERT INTO Usuarios (cpf, email, senha, nome, data_nascimento, genero, telefone, cep, numero, cidade, estado) VALUES
('46714567880', 'mmgaspargarcia@gmail.br', 'MarquinhoLindo24@', 'MARCO ANTONIO GASPAR GARCIA', '2002-08-29', 'M', '19982479747', '13400615', '330', 'PIRACICABA', 'SP'),
('46842958857', 'luizsoave@gmail.com', 'LuizEdu123!', 'LUIZ EDUARDO SOAVE', '2003-01-30', 'M', '19997301963', '13566580', '280', 'PIRACICABA', 'SP'),
('47814567291', 'ana.silva2023@gmail.com', 'AnaSilva#1!', 'ANA MARIA DA SILVA', '1995-03-15', 'F', '11998561234', '11025440', '120', 'SANTOS', 'SP'),
('49215789435', 'joaovitor_1998@hotmail.com', 'Joao123@', 'JOÃO VITOR SOUZA', '1998-07-22', 'M', '21997765432', '20561080', '450', 'RIO DE JANEIRO', 'RJ'),
('50324158760', 'carlos.oliveira@gmail.com', 'Carlos@2023', 'CARLOS HENRIQUE OLIVEIRA', '1992-11-10', 'M', '31996541234', '30140180', '300', 'BELO HORIZONTE', 'MG'),
('54817965412', 'pedrohenrique@gmail.com', 'Pedro2023!', 'PEDRO HENRIQUE MORAES', '1999-09-12', 'M', '21996452387', '21361040', '310', 'RIO DE JANEIRO', 'RJ'),
('57481236549', 'rafaelsilva@gmail.com', 'Rafael123!', 'RAFAEL SILVA PEREIRA', '1990-05-08', 'M', '41997751234', '40301500', '75', 'SALVADOR', 'BA'),
('52314589721', 'marianasantos@gmail.com', 'Mariana_321@', 'MARIANA SANTOS RIBEIRO', '2000-02-25', 'F', '11987451236', '13214000', '85', 'JUNDIAÍ', 'SP'),
('51247896300', 'julianaribeiro@gmail.com', 'Juliana@!234', 'JULIANA RIBEIRO DOS SANTOS', '1988-06-30', 'F', '21998561247', '22775470', '150', 'RIO DE JANEIRO', 'RJ'),
('55874123690', 'larissasouza@gmail.com', 'Larissa#123', 'LARISSA SOUZA DA COSTA', '1996-12-01', 'F', '31997851239', '30180170', '205', 'BELO HORIZONTE', 'MG'),
('58234718965', 'luanfernandes@gmail.com', 'Luan_2023@', 'LUAN FERNANDES DA SILVA', '1997-10-14', 'M', '11998562345', '13010100', '65', 'CAMPINAS', 'SP'),
('60325814790', 'gabriel.souza@gmail.com', 'Gabriel123@', 'GABRIEL SOUZA FERREIRA', '1994-09-05', 'M', '11999871234', '13504722', '15', 'RIO CLARO', 'SP'),
('59187423655', 'fernandaalmeida@gmail.com', 'Fernanda2023!', 'FERNANDA ALMEIDA MENDES', '1993-04-21', 'F', '31996458932', '30220160', '110', 'BELO HORIZONTE', 'MG');

INSERT INTO Medicos (crm, cpf, especialidade) VALUES
('123SP', '46842958857', 'NUTRÓLOGO'),
('12345SP', '47814567291', 'CARDIOLOGISTA'),
('124RJ', '49215789435', 'ORTOPEDISTA'),
('126SP', '54817965412', 'PEDIATRA'),
('127BA', '57481236549', 'CLÍNICO GERAL');

INSERT INTO Atendentes (cpf, data_contratacao) VALUES
('52314589721', '2020-03-15'),
('51247896300', '2019-05-10'),
('55874123690', '2022-12-01'),
('59187423655', '2023-02-20');

INSERT INTO Pacientes (cpf, convenio, altura, peso) VALUES
('46714567880', 'SANTA CASA SAÚDE', 1.82, 90.0),
('60325814790', 'UNIMED', 1.75, 75.0),
('50324158760', 'BRADESCO SAÚDE', 1.78, 82.5),
('58234718965', 'HAPVIDA', 1.60, 58.0);

INSERT INTO Alergias (paciente_cpf, alergia) VALUES
('46714567880', 'PICADA DE INSETOS'),
('50324158760', 'LACTOSE'),
('58234718965', 'FRUTOS DO MAR');

INSERT INTO Consultas (medico_crm, paciente_cpf, atendente_cpf, data_consulta, prontuario) VALUES 
('123SP', '46714567880', '52314589721', '2022-09-03 14:00:00', 'http//www.url1.com.br'),
('12345SP', '46714567880', '51247896300', '2023-12-10 16:00:00', 'http//www.url2.com.br'),
('124RJ', '46714567880', '55874123690', '2024-04-01 09:00:00', 'http//www.url3.com.br'),
('123SP', '46714567880', '52314589721', '2024-05-10 15:00:00', 'http//www.url4.com.br'),
('127BA', '46714567880', '59187423655', '2024-10-03 14:00:00', 'http//www.url5.com.br'),
('123SP', '46714567880', '52314589721', '2025-01-10 12:00:00', NULL),
('123SP', '50324158760', '52314589721', '2023-04-10 12:30:00', 'http//www.url6.com.br'),
('127BA', '50324158760', '59187423655', '2024-08-20 11:00:00', 'http//www.url7.com.br'),
('124RJ', '50324158760', '55874123690', '2025-02-15 09:00:00', NULL);




