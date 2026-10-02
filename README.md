# Personal Finance Manager

Plataforma pessoal de controle financeiro desenvolvida com Django.

O projeto começou como TaskFlow, uma aplicação de gerenciamento de projetos
usada durante a Fase 1 de aprendizado. Na Fase 2, o repositório evoluirá
gradualmente para um gerenciador pessoal de despesas.

A versão da Fase 1 permanece preservada pela tag `v0.1.0`.

## Estado atual

O projeto está na Fase 2.

O domínio legado do TaskFlow foi removido. A aplicação preserva autenticação, usuários, PostgreSQL, testes, CI, Docker e a configuração de produção construídos durante a Fase 1.

Enquanto o domínio financeiro ainda não foi implementado, usuários autenticados acessam uma home temporária.

## Objetivo da V1

A primeira versão do produto permitirá que cada usuário:

- registre receitas e despesas;
- organize transações por categorias;
- consulte seu histórico financeiro por período;
- visualize totais de receitas, despesas e resultado;
- acesse somente seus próprios dados financeiros.

## Fora do escopo da V1

A V1 não inclui:

- contas bancárias e transferências;
- cartões de crédito e faturas;
- parcelas e transações recorrentes;
- orçamentos, metas e previsões;
- importação de CSV ou OFX;
- integração com Open Finance;
- React;
- Celery, Redis ou microserviços.

## Tecnologias

- Python 3.13
- Django 6.1
- PostgreSQL 18.6
- Docker e Docker Compose
- Gunicorn
- Ruff
- GitHub Actions
- WhiteNoise

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

    - Aplicação: http://127.0.0.1:8000/
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

As mesmas verificações podem ser executadas por um único script:

```bash
./scripts/check.sh
```

Para também construir a imagem de produção ao final das verificações:

```bash
./scripts/check.sh --production
```

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

As variáveis `TASKFLOW_DB_NAME`, `TASKFLOW_DB_USER`, `TASKFLOW_DB_HOST`, `TASKFLOW_DB_PORT` e `TASKFLOW_DB_SSLMODE` também podem ser configuradas. Em produção, `TASKFLOW_DB_SSLMODE` usa `require` por padrão.

A imagem executa a aplicação com Gunicorn e um usuário sem privilégios. Segredos não são copiados para a imagem. WhiteNoise entrega os arquivos estáticos, enquanto a infraestrutura fornece PostgreSQL e HTTPS.

## Estratégia de migrations e rollback

As migrations `0001` a `0005` preservam o histórico de evolução do TaskFlow.

A migration `0006` remove os models e as tabelas de Project e Task. Os dados eram sintéticos e sua exclusão foi aceita durante a transição para a Fase 2. Usuários e autenticação não são removidos.

Reverter a migration `0006` pode recriar a estrutura das tabelas, mas não recupera os registros apagados. O código da Fase 1 permanece disponível pela tag `v0.1.0`.

O app `projects` permanece temporariamente instalado para que o Django possa carregar seu histórico de migrations.

## Segurança e tratamento de dados

Desenvolvimento, testes e staging utilizam somente dados sintéticos.

Consulte a [política de tratamento de dados financeiros](docs/security/data-handling.md) antes de trabalhar com exports, backups, credenciais ou dados reais.
