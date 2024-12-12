#!/bin/bash
# Aguarda o banco de dados ficar disponível
while ! nc -z $DB_HOST $DB_PORT; do
  echo "Aguardando banco de dados..."
  sleep 2
done

echo "Banco de dados disponível. Executando migrações..."
python manage.py makemigrations
python manage.py migrate --fake

echo "Iniciando servidor Django..."
exec "$@"
