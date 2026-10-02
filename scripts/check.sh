#!/usr/bin/env bash

set -euo pipefail

run_production=false

if (( $# > 1 )); then
    echo "Uso: $0 [--production]" >&2
    exit 2
fi

if (( $# == 1 )); then
    if [[ "$1" != "--production" ]]; then
        echo "Opção desconhecida: $1" >&2
        echo "Uso: $0 [--production]" >&2
        exit 2
    fi

    run_production=true
fi

echo "Executando lint..."
docker compose exec web ruff check .

echo "Verificando formatação..."
docker compose exec web ruff format --check .

echo "Executando verificações do Django..."
docker compose exec web python manage.py check

echo "Verificando migrations pendentes..."
docker compose exec web python manage.py makemigrations --check --dry-run

echo "Executando testes..."
docker compose exec web python manage.py test --shuffle

if [[ "$run_production" == true ]]; then
    echo "Construindo imagem de produção..."
    docker build \
        --file Dockerfile.production \
        --tag taskflow-production:local \
        .
fi

echo "Todas as verificações passaram."
