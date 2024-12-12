# Dok - Sistema de Gerenciamento de Consultas Médicas
Projeto final da disciplina SSC0621 - Modelagem Orientada a Objetos.

**Docente:** Profa. Dra. Lina María Garcés Rodríguez

## Alunos 
- Leonardo Gueno Rissetto (13676482)
- Lucas Lima Romero (13676325)
- Luciano Gonçalves Lopes Filho (13676520)
- Marco Antonio Gaspar Garcia (11833581)
- Thiago Kashivagui Gonçalves (13676579)

## Descrição do Sistema
**Dok** é uma plataforma online que busca facilitar o agendamento de consultas médicas, pode ser facilmente amplamente adotado, tanto por médicos quanto por pacientes de todo o Brasil. A ideia principal é fornecer um Hub com todas as informações necessárias para o agendamento e o gerenciamento de consultas médicas, em que os médicos possam organizar sua rotina de atendimentos de forma prática e que os pacientes possam acessar rapidamente informações sobre suas consultas. 

Na versão atual, o Dok permite a pesquisa de todo o histórico de consultas médicas realizadas por cada pessoa.

## Pré-requisitos
A única dependência necessária para executar esta aplicação é o **Docker**. O Docker é uma plataforma de contêinerização que facilita a criação, execução e gerenciamento de contêineres para aplicações. Certifique-se de que ele está instalado em sua máquina antes de prosseguir. 

## Como utilizar o sistema

Primeiramente, caso seja a primeira execução, execute o seguinte comando na raiz do diretório:
```bash
docker compose up --build
```
A flag ```--build``` força a reconstrução das imagens, mas não é necessária em execuções posteriores, pois a imagem já estará construída.

Esse comando inicia os contêineres do PostgreSQL, que contém o banco de dados, e do Django, que é responsável pelo servidor do site e pela aplicação em si. A comunicação entre os contêineres é orquestrada pelo Django, framework de desenvolvimento de **backend** de sites em **Python**. 

Com os contêineres rodando, rode a aplicação acessando em seu navegador o localhost:

[http://127.0.0.1:8000/](http://127.0.0.1:8000/)


Para parar a execução do servidor, simplesmente mate o processo com ```CTRL + C```. Além disso, caso deseje-se apagar completamente as informações, isto é, remover os volumes criados pelos contêineres, execute:

```bash
docker compose down -v
```