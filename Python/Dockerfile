# Usando a imagem oficial do Python
FROM python:3.9-slim

# Instalar dependências do sistema para o psycopg2
RUN apt-get update && apt-get install -y \
    build-essential \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*  # Limpar o cache do apt para reduzir o tamanho da imagem

# Diretório de trabalho dentro do container
WORKDIR /app

# Copiar o arquivo requirements.txt para dentro do container
COPY requirements.txt .

# Instalar as dependências do Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar todos os arquivos do diretório local para o container
COPY . .

# Comando para rodar o script Python
CMD ["python", "/app/app/sistema.py"]