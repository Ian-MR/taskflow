# TaskFlow

Aplicação web para gerenciamento de projetos e tarefas, desenvolvida como projeto de estudo de Django e engenharia de backend.

O projeto cobre autenticação e autorização, PostgreSQL, testes automatizados, otimização de queries, CI, Docker e preparação para produção.

## Tecnologias

- Python 3.13
- Django 6.1
- PostgreSQL 18.6
- Docker e Docker Compose
- Gunicorn
- Ruff
- GitHub Actions

## Requisitos

- Git
- Docker Engine
- Docker Compose v2 (`docker compose`)

## Como executar localmente

1. Clone o repositório:

    ```bash
    git clone https://github.com/Ian-MR/taskflow.git
    cd taskflow
    ```

2. Crie o arquivo de variáveis de ambiente:

    ```bash
    cp .env.example .env
    ```

3. Edite o `.env` e substitua os valores `replace-me`, principalmente `TASKFLOW_DB_PASSWORD` e `TASKFLOW_SECRET_KEY`.

4. Construa e inicie os containers:

    ```bash
    docker compose up --build -d
    ```
5. Aplique as migrations:

    ```bash
    docker compose exec web python manage.py migrate
    ```

6. Crie um usuário administrador:

    ```bash
    docker compose exec web python manage.py createsuperuser
    ```

7. Acesse:

    - Aplicação: http://127.0.0.1:8000/projects/
    - Healthcheck: http://127.0.0.1:8000/health/

## Comandos úteis

Iniciar os serviços em segundo plano:

```bash
docker compose up -d
```

Verificar o estado dos containers:

```bash
docker compose ps
```

Acompanhar os logs da aplicação:

```bash
docker compose logs -f web
```

Abrir o shell do Django:

```bash
docker compose exec web python manage.py shell
```

Parar e remover os containers:

```bash
docker compose down
```

O comando `docker compose down` preserva o volume do PostgreSQL. Usar `docker compose down -v` também apaga o volume e os dados locais.

## Testes e qualidade

Com os serviços em execução, rode:

```bash
docker compose exec web ruff check .
docker compose exec web ruff format --check .
docker compose exec web python manage.py check
docker compose exec web python manage.py makemigrations --check --dry-run
docker compose exec web python manage.py test --shuffle
```

O pipeline de CI executa lint, verificação de formatação, checks do Django, verificação de migrations, testes com PostgreSQL e build da imagem de produção.

## Configuração de produção

A aplicação possui settings separados:

- `config.settings.development` para desenvolvimento local;
- `config.settings.production` para staging e produção.

A imagem de produção é construída com:

```bash
docker build --file Dockerfile.production --tag taskflow-production:local .
```

A configuração de produção exige estas variáveis:

- `TASKFLOW_SECRET_KEY`
- `TASKFLOW_DB_PASSWORD`
- `TASKFLOW_ALLOWED_HOSTS`: hosts separados por vírgula;
- `TASKFLOW_SECURE_HSTS_SECONDS`: duração do HSTS em segundos.

As variáveis `TASKFLOW_DB_NAME`, `TASKFLOW_DB_USER`, `TASKFLOW_DB_HOST` e `TASKFLOW_DB_PORT` também podem ser configuradas para apontar para o PostgreSQL do ambiente.

A imagem executa a aplicação com Gunicorn e um usuário sem privilégios. Segredos não são copiados para a imagem. A infraestrutura de produção também deve fornecer PostgreSQL, HTTPS e a entrega dos arquivos estáticos.

## Estratégia de migrations e rollback

A obrigatoriedade do proprietário de um projeto foi implementada em etapas compatíveis:

1. **Expand:** a migration `0003` adicionou `owner` permitindo `NULL`.
2. **Switch:** a aplicação passou a associar novos projetos ao usuário autenticado.
3. **Migrate:** a migration `0004` atribuiu um usuário técnico aos registros legados sem proprietário.
4. **Contract:** a migration `0005` tornou `owner_id` obrigatório no banco.

Antes de migrations em produção, deve ser criado e validado um backup do banco.

O rollback da aplicação deve reutilizar a imagem anterior identificada por tag ou digest, sem reconstruí-la. O rollback do banco exige análise separada:

- a `0005` pode voltar a permitir `NULL`;
- a `0004` possui reverse migration sem operação;
- proprietários atribuídos durante o backfill não são removidos automaticamente, pois isso poderia apagar uma associação válida.

Portanto, voltar o código não significa necessariamente desfazer os dados.
Migrations destrutivas exigem uma estratégia específica de recuperação.
