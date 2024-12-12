# Use uma imagem do Python
FROM python:3.10-slim

# Instalar dependências do sistema
RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    apt-get clean

# Definir o diretório de trabalho
WORKDIR /app

# Copiar o requirements.txt e instalar dependências
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copiar o código do Django
COPY . /app/

# Expor a porta 8000 para o servidor Django
EXPOSE 8000