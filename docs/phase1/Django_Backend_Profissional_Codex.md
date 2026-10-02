# Django Backend Profissional — Guia de Aprendizado com Codex CLI

> **Objetivo:** aprender Django, engenharia de backend e Docker em 7–10 dias sem terceirizar o aprendizado para o agente.
>
> **Stack-base:** Django 6.1 · Python 3.13 · PostgreSQL · Docker/Compose · Git/GitHub · Ruff · testes · CI/CD · deploy.

## Como este repositório deve ser usado com o Codex

Este guia foi adaptado para um fluxo de **pair programming educacional**. O Codex é um mentor e revisor, não o autor principal do projeto.

A regra central é:

> **Eu escrevo a implementação. O Codex me ajuda a entender, diagnosticar, testar, questionar decisões e revisar o resultado.**

O arquivo [`AGENTS.md`](./AGENTS.md) contém as instruções operacionais que o Codex CLI deve seguir automaticamente neste repositório. Este arquivo contém o conteúdo de estudo e os critérios técnicos.

### Modos de trabalho

#### 1. Mentor — padrão

Use para estudar um conceito ou decidir como implementar algo.

O Codex deve:

1. explicar o conceito e o problema que ele resolve;
2. relacioná-lo ao TaskFlow e aos arquivos relevantes do repositório;
3. fazer perguntas que testem seu entendimento quando isso ajudar;
4. sugerir a próxima pequena etapa;
5. oferecer **hints progressivos**, em vez de entregar a solução completa;
6. depois que você implementar, revisar o diff e explicar o que melhoraria.

Exemplo de pedido:

```text
Estou no Dia 3. Quero implementar criação de projetos com ModelForm.
Não implemente por mim. Explique o fluxo, me diga quais arquivos devo tocar
e me dê os critérios que minha solução precisa cumprir.
```

#### 2. Debugger — diagnóstico antes da correção

Use quando algo não funciona.

A sequência ideal é:

```text
reproduzir → coletar evidência → formular hipótese → localizar causa → eu corrijo → retestar
```

O Codex pode ler o código, executar testes, lint e comandos de diagnóstico não destrutivos. Ele **não deve editar os arquivos para corrigir o bug por padrão**.

Peça assim:

```text
Diagnostique este bug sem alterar os arquivos.
Reproduza se possível, identifique a causa-raiz, mostre a evidência
e me dê primeiro uma pista, não a solução completa.
```

Se você travar, peça uma pista mais forte. Esse mecanismo evita transformar debugging em copiar patch.

#### 3. Revisor sênior de PR

Quando a feature estiver pronta, peça uma revisão completa:

```text
Revise minha branch como um engenheiro backend sênior.
Não altere nenhum arquivo.
Compare com main, rode os checks relevantes e trate isto como uma PR real.
```

A revisão deve priorizar:

- correção funcional e casos de borda;
- autenticação, autorização e IDOR;
- integridade de dados, migrations e compatibilidade de deploy;
- transações e concorrência quando relevantes;
- consultas ORM, N+1 e custo de banco;
- qualidade e suficiência dos testes;
- legibilidade, coesão, acoplamento e abstrações desnecessárias;
- contratos HTTP/API;
- segredos e configuração por ambiente;
- Docker, CI/CD e comportamento de produção quando tocados pela mudança;
- logs/observabilidade quando relevantes.

Cada achado deve ter severidade, localização, impacto e direção de correção. O Codex não deve fabricar problemas apenas para parecer rigoroso.

### Escada de ajuda

Quando você estiver aprendendo, prefira esta ordem:

1. **Pergunta orientadora** — ajuda você a perceber o problema.
2. **Pista conceitual** — aponta o conceito relevante.
3. **Pista estrutural** — indica arquivo/camada/fluxo.
4. **Pseudocódigo ou trecho mínimo** — mostra a forma sem entregar a feature inteira.
5. **Solução completa** — somente se você pedir explicitamente ou se a finalidade deixar de ser aprendizado.

### Registro de progresso

Mantenha [`LEARNING_PROGRESS.md`](./LEARNING_PROGRESS.md) atualizado. No começo de uma sessão, diga ao Codex o dia atual e o objetivo. No final, registre:

- o que você implementou;
- o que consegue explicar sem consultar;
- bugs encontrados e causa-raiz;
- decisões de arquitetura e trade-offs;
- pontos apontados na revisão da PR;
- tema que precisa rever.

---

# 1. Como usar este guia

Este material foi desenhado para estudo intensivo, mas também para continuar servindo como referência depois dos 10 dias.

> **META PRINCIPAL:** ao final, você deve conseguir criar, testar, versionar, containerizar e publicar uma aplicação Django pequena sem depender de copiar um tutorial passo a passo.

O objetivo de 10 dias não é “dominar Django por completo”. É construir um modelo mental sólido. Você deve sair sabendo onde procurar, por que uma decisão existe e quais erros evitar.

## O método de estudo

- 30–40 min de conceito e documentação oficial.
- 90–120 min de implementação no projeto TaskFlow.
- 20–30 min tentando quebrar o que você acabou de construir: entradas inválidas, permissões, banco indisponível, testes falhando.
- 20–30 min de refatoração e registro do que aprendeu.
> **REGRA DE RETENÇÃO:** leia uma ideia, feche a referência e tente implementá-la de memória. Consulte novamente apenas quando travar. Copiar tutorial produz sensação de progresso; reconstruir produz aprendizado.

## O projeto único: TaskFlow

Você aprenderá tudo em um único sistema de gerenciamento de projetos e tarefas. Isso evita o erro de fazer vários CRUDs desconectados e permite observar como decisões iniciais afetam o código depois.

| Módulo | Responsabilidade |
| --- | --- |
| accounts | autenticação, usuário e permissões |
| projects | projetos e participação |
| tasks | tarefas, status e responsáveis |
| core/config | configuração global, URLs e settings |

## Critério de sucesso

- Você consegue explicar o caminho request → URL → view → serviço/regra → ORM → banco → response.
- Você consegue adicionar uma feature usando branch, testes e Pull Request.
- Você consegue iniciar aplicação + PostgreSQL com Docker Compose.
- Você sabe por que local, teste, staging e produção são ambientes diferentes.
- Você sabe fazer um deploy básico sem usar runserver e sabe quais verificações executar antes.
# 2. O modelo mental do Django

Antes de decorar arquivos, entenda o fluxo. Django é uma aplicação HTTP que recebe uma requisição, executa código e devolve uma resposta.

```text
Cliente / navegador
      | HTTP
      v
urls.py -> view -> regra de negócio -> ORM -> PostgreSQL
      |                                  |
      +---------- response <-------------+
```

## Request e response

Uma requisição HTTP possui método, caminho, headers, cookies e possivelmente corpo. O Django a representa com HttpRequest. A view recebe esse objeto e devolve um HttpResponse — diretamente ou por helpers como render() e redirect().

## Project x app

| Conceito | Pense como | Exemplo |
| --- | --- | --- |
| Project | a aplicação completa e sua configuração | TaskFlow |
| App | um módulo de domínio reutilizável/coeso | tasks, projects, accounts |

> **BOA PRÁTICA:** organize apps por domínio ou responsabilidade de negócio. Evite criar apps técnicos demais como models_app, views_app ou utils_app.

## Onde colocar lógica?

| Camada | Responsabilidade | Evite |
| --- | --- | --- |
| View | adaptar HTTP, autorização e orquestração | regras extensas e queries repetidas |
| Form/Serializer | validar e transformar entrada | efeitos colaterais complexos |
| Model | estado, invariantes e comportamento ligado ao dado | virar um “Deus model” |
| QuerySet/Manager | consultas reutilizáveis e expressivas | regras de workflow |
| Service (quando necessário) | orquestração de caso de uso com múltiplos efeitos | criar uma camada para cada CRUD simples |
| Template | apresentação | regra de negócio |

> **PRINCÍPIO:** comece idiomático em Django. Abstraia quando a duplicação ou complexidade aparecer. “Clean Architecture” aplicada mecanicamente pode apenas mover complexidade para mais arquivos.

# 3. Stack e ferramentas deste aprendizado

A intenção é reduzir decisões irrelevantes e usar um conjunto coerente de ferramentas.

| Ferramenta | Uso | Por que agora |
| --- | --- | --- |
| Python 3.13 | runtime | compatível com Django 6.1 e estável para estudo |
| Django 6.1 | framework web | versão estável atual deste guia |
| PostgreSQL | banco relacional | recomendado pelo próprio Django para produção |
| Git + GitHub | versionamento e colaboração | branches, PRs e histórico |
| Ruff | lint + formatação | feedback rápido e configuração simples |
| Docker | empacotamento | ambiente reproduzível |
| Docker Compose | app + banco local | orquestra múltiplos containers |
| GitHub Actions | CI | executa checks/testes em cada PR |
| Gunicorn ou Uvicorn | servidor de aplicação | runserver não é servidor de produção |

## Dependências: mantenha simples no início

Nos primeiros dias, use venv + pip. O aprendizado importante é isolamento e reprodutibilidade. Depois você pode migrar para ferramentas como uv ou Poetry, mas não deixe o gerenciador de dependências virar o assunto principal.

```bash
python -m venv .venv
# ativar o ambiente
python -m pip install Django==6.1
python -m pip freeze > requirements.txt
```

# 4. Roadmap de 10 dias

Cada dia combina uma competência Django com uma prática de engenharia. Assim, qualidade não vira uma “fase final”.

| Dia | Django | Engenharia |
| --- | --- | --- |
| 1 | HTTP, project/app, URLs e views | venv, Git, .gitignore, commits |
| 2 | models, migrations e ORM | PostgreSQL e modelagem |
| 3 | templates, forms e CRUD | settings, .env e configuração |
| 4 | auth e autorização | branches, PR e revisão |
| 5 | queries e organização de código | Ruff, pre-commit e refatoração |
| 6 | testes Django | ambiente de teste e estratégia |
| 7 | testes de integração e performance ORM | CI com GitHub Actions |
| 8 | API/HTTP mais profundo | Docker e Docker Compose |
| 9 | hardening e preparação de produção | staging, static files e logs |
| 10 | refatoração e release | deploy, migrations, rollback e tag |

> **SE SÓ TIVER 7 DIAS:** junte 3+4, 5+6 e 9+10. Não corte testes, Git, Docker ou deploy; reduza a profundidade.

# 5.1. Dia 1 — Fundamentos, HTTP e primeiro fluxo

Entender o que acontece quando uma URL é acessada e iniciar o repositório corretamente.

## Conceitos a dominar

- HTTP: GET/POST, status code, request e response
- startproject, startapp, urls.py, views.py
- venv, dependências, .gitignore
- Git: working tree, staging area, commit, branch
## Prática obrigatória

- Criar repositório taskflow e ambiente .venv.
- Criar projeto Django e app projects.
- Implementar /health/ retornando JSON e /projects/ retornando uma resposta simples.
- Fazer commits pequenos com mensagens descritivas.
## Saída do dia

- [ ] Explica request → URLconf → view → response sem consultar.
- [ ] Consegue recriar o projeto em uma pasta vazia.
- [ ] git status está limpo e .venv/.env não são versionados.
```bash
python -m venv .venv
python -m pip install Django==6.1
django-admin startproject config .
python manage.py startapp projects
python manage.py runserver
```

# 5.2. Dia 2 — Models, migrations, ORM e PostgreSQL

Modelar dados e entender a relação entre classe Python, migration, schema e consulta SQL.

## Conceitos a dominar

- Model, Field, ForeignKey, constraints
- makemigrations x migrate
- QuerySet é lazy; filter/get/create/update/delete
- índices, unicidade e integridade referencial
## Prática obrigatória

- Criar Project, Task e relações.
- Praticar queries no Django shell.
- Subir PostgreSQL local (instalação nativa por enquanto, se preferir).
- Inspecionar pelo menos uma query com .query ou ferramenta de debug.
## Saída do dia

- [ ] Sabe quando usar ForeignKey/ManyToMany.
- [ ] Não trata migration como “arquivo descartável”.
- [ ] Entende que QuerySet não é uma lista comum.
```python
python manage.py makemigrations
python manage.py migrate
python manage.py shell

# No shell
Project.objects.create(name="Projeto de estudo")
Project.objects.filter(name__icontains="estudo")
```

# 5.3. Dia 3 — Forms, templates e configuração por ambiente

Construir CRUD e separar código de configuração de segredos.

## Conceitos a dominar

- render/context/template inheritance
- Form e ModelForm; validação
- settings base/local/test/production
- variáveis de ambiente e .env.example
## Prática obrigatória

- Criar lista/detalhe/criação/edição de projetos.
- Criar base.html.
- Mover SECRET_KEY e credenciais para ambiente.
- Criar .env.example sem segredos.
## Saída do dia

- [ ] Nenhum segredo no Git.
- [ ] Validação importante existe no backend, não só HTML.
- [ ] Consegue dizer o que muda entre local e produção.
# 5.4. Dia 4 — Autenticação, autorização e GitHub Flow

Fazer a aplicação respeitar identidade e permissão; praticar fluxo de mudança isolada.

## Conceitos a dominar

- Authentication x authorization
- request.user, login_required, permissions
- branch curta, Pull Request, code review
- squash merge e main protegida
## Prática obrigatória

- Adicionar owner ao Project.
- Usuário B não pode alterar projeto de A.
- Criar feat/project-permissions.
- Abrir PR, revisar diff e fazer squash merge.
## Saída do dia

- [ ] Tem teste/manual proof de autorização.
- [ ] main fica sempre potencialmente deployável.
- [ ] Não trabalha features diretamente na main.
# 5.5. Dia 5 — Código sustentável e qualidade automática

Aprender a perceber código ruim antes de ele crescer.

## Conceitos a dominar

- coesão, acoplamento, SRP de forma pragmática
- QuerySet/Manager para consultas repetidas
- services apenas para casos de uso relevantes
- lint, format e imports
## Prática obrigatória

- Configurar Ruff.
- Refatorar ao menos uma query repetida.
- Quebrar uma view grande em funções/camadas coerentes.
- Eliminar nomes vagos e duplicação evidente.
## Saída do dia

- [ ] Ruff passa sem erro.
- [ ] Você consegue justificar cada abstração criada.
- [ ] Não existe services.py vazio “porque arquitetura manda”.
```toml
[tool.ruff]
line-length = 100

[tool.ruff.lint]
select = ["E", "F", "I", "B"]
```

# 5.6. Dia 6 — Testes que protegem comportamento

Criar uma suíte pequena, confiável e independente.

## Conceitos a dominar

- Arrange–Act–Assert
- SimpleTestCase/TestCase/TransactionTestCase
- test database isolado
- model, form, permission, view tests
## Prática obrigatória

- Testar criação de projeto.
- Testar entrada inválida.
- Testar usuário anônimo e usuário sem permissão.
- Testar fluxo principal com Django Client.
## Saída do dia

- [ ] Testes não dependem de ordem.
- [ ] Cada teste cria seus próprios dados relevantes.
- [ ] Uma regressão de permissão faz a suíte falhar.
```python
from django.test import TestCase

class ProjectPermissionTests(TestCase):
    def test_other_user_cannot_edit_project(self):
        # Arrange
        ...
        # Act
        ...
        # Assert
        self.assertEqual(response.status_code, 403)
```

# 5.7. Dia 7 — Integração, ORM eficiente e CI

Conectar qualidade local a um pipeline automático.

## Conceitos a dominar

- N+1, select_related e prefetch_related
- transações e atomicidade
- CI: checkout → install → lint → check → migration check → tests
- PostgreSQL como service container
## Prática obrigatória

- Identificar e corrigir um N+1.
- Criar workflow do GitHub Actions.
- Rodar testes contra PostgreSQL no CI.
- Impedir merge quando CI falhar.
## Saída do dia

- [ ] PR mostra check verde antes de merge.
- [ ] Sabe explicar CI versus CD.
- [ ] Sabe por que testar no mesmo engine de banco é valioso.
```bash
ruff check .
ruff format --check .
python manage.py check
python manage.py makemigrations --check --dry-run
python manage.py test
```

# 5.8. Dia 8 — Docker e Docker Compose

Tornar o ambiente reproduzível e entender o isolamento por containers.

## Conceitos a dominar

- image, container, Dockerfile, layer
- volume x bind mount
- network e DNS de serviço
- Compose: web + db
## Prática obrigatória

- Criar .dockerignore.
- Criar Dockerfile de desenvolvimento simples.
- Criar compose.yaml com web e postgres.
- Adicionar volume de banco e healthcheck.
## Saída do dia

- [ ] docker compose up inicia stack completa.
- [ ] Django acessa banco pelo nome do serviço, não localhost.
- [ ] Você sabe o que é persistido e o que é descartável.
```yaml
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    ports:
      - "8000:8000"
    depends_on:
      db:
        condition: service_healthy

  db:
    image: postgres:17
    environment:
      POSTGRES_DB: taskflow
      POSTGRES_USER: taskflow
      POSTGRES_PASSWORD: local-only
    healthcheck:
      test: ["CMD-SHELL", "pg_isready -U taskflow"]
      interval: 5s
      timeout: 3s
      retries: 10
    volumes:
      - postgres_data:/var/lib/postgresql/data

volumes:
  postgres_data:
```

# 5.9. Dia 9 — Produção, segurança e staging

Entender o que muda quando a aplicação fica exposta à internet.

## Conceitos a dominar

- DEBUG=False, ALLOWED_HOSTS, SECRET_KEY
- HTTPS, cookies secure, CSRF
- collectstatic e static files
- logs, healthcheck, staging
## Prática obrigatória

- Criar settings de produção.
- Executar check --deploy.
- Construir uma imagem de produção sem runserver.
- Definir ambiente staging separado do production.
## Saída do dia

- [ ] Nenhum segredo na imagem/repo.
- [ ] runserver não aparece no plano de produção.
- [ ] Consegue listar diferenças de staging e production.
```bash
python manage.py check --deploy --settings=config.settings.production
python manage.py collectstatic --noinput
```

# 5.10. Dia 10 — Release, deploy seguro e rollback

Fechar o ciclo completo de mudança: código → release → produção → recuperação.

## Conceitos a dominar

- artefato imutável
- tag/SemVer
- migrations compatíveis e expand/contract
- backup, rollback e observabilidade
## Prática obrigatória

- Passar checklist final.
- Criar tag v0.1.0.
- Deployar em uma plataforma escolhida.
- Simular rollback para a versão anterior.
## Saída do dia

- [ ] Você consegue repetir o deploy sem editar servidor “na mão”.
- [ ] Sabe como voltar se uma release quebrar.
- [ ] README permite outra pessoa iniciar o projeto.
# 6. Arquitetura recomendada do projeto

Estrutura é uma ferramenta de comunicação. A melhor estrutura é a mais simples que deixa claro onde cada responsabilidade vive.

```text
taskflow/
├── config/
│   ├── settings/
│   │   ├── base.py
│   │   ├── local.py
│   │   ├── test.py
│   │   └── production.py
│   ├── urls.py
│   ├── asgi.py
│   └── wsgi.py
├── accounts/
├── projects/
│   ├── migrations/
│   ├── models.py
│   ├── forms.py
│   ├── views.py
│   ├── urls.py
│   ├── services.py       # só se houver caso de uso que justifique
│   ├── selectors.py      # opcional; consultas complexas/reutilizadas
│   └── tests/
├── tasks/
├── templates/
├── static/
├── .env.example
├── .gitignore
├── .dockerignore
├── Dockerfile
├── compose.yaml
├── pyproject.toml
├── requirements.txt
├── README.md
└── manage.py
```

## Heurística: onde essa lógica deveria ficar?

- Se existe porque chegou uma requisição HTTP → view.
- Se valida campos/entrada → Form/Serializer.
- Se expressa uma consulta de negócio reutilizada → QuerySet/Manager ou selector.
- Se preserva uma invariante do próprio objeto → model.
- Se coordena vários objetos/efeitos externos em um caso de uso → service.
- Se existe só para desenhar HTML → template.
> **CHEIRO DE CÓDIGO:** “utils.py” crescendo sem tema claro normalmente indica responsabilidades sem dono. Dê nomes de domínio ou mova a lógica para a camada que realmente a possui.

# 7. Ambientes e configuração

Ambiente é o conjunto de recursos e configurações em que o mesmo software roda. O código deve permanecer essencialmente o mesmo; o que muda são valores, serviços e políticas.

| Ambiente | Objetivo | Dados | Características |
| --- | --- | --- | --- |
| local | desenvolver rápido | descartáveis/locais | DEBUG=True, hot reload |
| test | validar automaticamente | banco temporário | determinístico, sem dependência externa desnecessária |
| staging | ensaiar produção | separados/falsos/anonimizados | DEBUG=False, infraestrutura parecida com produção |
| production | usuários reais | reais e protegidos | HTTPS, backups, monitoramento, segredos reais |

## 12-factor na prática: configuração por ambiente

Não coloque segredos, URLs específicas de produção ou senhas no código. Leia-os de variáveis de ambiente. Um arquivo .env pode ajudar localmente, mas ele é uma conveniência local, não um cofre de segredos.

```text
# .env.example
DJANGO_SECRET_KEY=
DATABASE_URL=
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1
```

> **NUNCA VERSIONE:** .env real, SECRET_KEY de produção, senhas, tokens de cloud, chaves privadas, dumps de banco com dados reais.

## Settings separados: use sem duplicar tudo

```python
# config/settings/base.py
DEBUG = False

# config/settings/local.py
from .base import *
DEBUG = True

# config/settings/production.py
from .base import *
DEBUG = False
# cookies seguros, hosts, storage, logging etc.
```

# 8. Docker: o que você realmente precisa aprender

Docker não é “uma máquina virtual menor”. Para seu objetivo, pense nele como uma forma padronizada de construir e executar processos com filesystem e dependências controlados.

## Conceitos essenciais

| Conceito | Definição prática | No TaskFlow |
| --- | --- | --- |
| Image | template imutável construído a partir do Dockerfile | Python + deps + código |
| Container | instância em execução de uma image | processo Django |
| Dockerfile | receita de build da image | como instalar e iniciar a app |
| Layer | camada reutilizável do build/cache | COPY requirements antes do código ajuda cache |
| Volume | armazenamento persistente gerenciado | dados do PostgreSQL |
| Bind mount | pasta do host montada no container | código local durante desenvolvimento |
| Network | rede virtual entre serviços | web acessa db pelo hostname db |
| Compose | declara vários serviços juntos | web + db |

## Dockerfile de aprendizado

```dockerfile
FROM python:3.13-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
```

> **IMPORTANTE:** este CMD com runserver é aceitável para o container de desenvolvimento. Para produção, troque por um servidor WSGI/ASGI apropriado.

## Por que app e banco ficam em containers diferentes?

- Cada processo tem ciclo de vida próprio: você pode recriar a aplicação sem apagar o banco.
- Escala e manutenção ficam independentes.
- Persistência do banco fica explícita em um volume.
- Compose fornece rede e DNS entre os serviços.
## O erro clássico de localhost

Dentro do container web, localhost aponta para o próprio container web. Se o PostgreSQL é outro serviço do Compose, use o nome do serviço (por exemplo, db) como hostname.

## Persistência: container é descartável; dado não

```bash
docker compose up -d
docker compose logs -f web
docker compose exec web python manage.py migrate
docker compose down        # remove containers, preserva volume nomeado
docker compose down -v     # também remove volumes: cuidado, apaga dados locais
```

## Boas práticas de build que você aprenderá depois do primeiro sucesso

- Crie .dockerignore para não enviar .git, .venv, caches e segredos ao contexto de build.
- Ordene COPY/RUN para aproveitar cache de dependências.
- Em produção, rode o processo como usuário não-root sempre que possível.
- Use imagens pequenas, mas não sacrifique depuração e segurança por “menor tamanho” sem entender o trade-off.
- Não grave dados mutáveis importantes na camada gravável do container.
# 9. Git e versionamento: fluxo recomendado

Para um projeto individual ou equipe pequena, um fluxo leve costuma ensinar mais e gerar menos burocracia que Git Flow completo.

```text
main
  ├─ feat/project-permissions
  ├─ feat/task-filter
  ├─ fix/duplicate-task
  └─ refactor/task-queryset
```

## Ciclo de uma mudança

1. Atualize main.
1. Crie uma branch curta com objetivo único.
1. Implemente em commits compreensíveis.
1. Rode checks/testes localmente.
1. Abra Pull Request.
1. Leia o próprio diff como revisor.
1. Espere CI verde.
1. Squash merge e apague a branch.
## Commits úteis

```text
feat: add project creation
fix: block editing projects from other users
test: cover task ownership permissions
refactor: extract pending task queryset
docs: document local setup
chore: configure ruff
```

> **NÃO CONFUNDA:** commit é unidade de histórico; branch é linha isolada de trabalho; PR é proposta/revisão de mudança; release/tag é uma versão publicada.

## Semantic Versioning como referência

```text
v1.4.2
 | | |
 | | +-- PATCH: correção compatível
 | +---- MINOR: funcionalidade compatível
 +------ MAJOR: mudança incompatível
```

Antes de 1.0, versões 0.x podem ser usadas enquanto a API e a estrutura ainda estão amadurecendo. Para seu projeto, v0.1.0 é uma boa primeira release demonstrável.

# 10. Estratégia de testes

O objetivo não é perseguir um número de cobertura. É reduzir medo de mudança protegendo comportamentos importantes.

## Tipos

| Tipo | Escopo | Exemplo |
| --- | --- | --- |
| unitário | função/regra pequena sem infraestrutura | calcular transição de status |
| integração | partes reais trabalhando juntas | service + ORM + PostgreSQL |
| web/API | request até response usando test client | POST /projects/ respeita permissão |
| E2E | sistema pelo ponto de vista do usuário | login → cria projeto → cria tarefa |

## Banco de teste

O Django cria um banco de testes separado. Em bancos como PostgreSQL, por padrão o nome deriva do banco configurado. Testes que usam banco devem usar as classes Django adequadas, mantendo isolamento entre casos.

## Arrange – Act – Assert

```python
def test_owner_can_edit_project(self):
    # Arrange
    project = Project.objects.create(owner=self.user, name="A")

    # Act
    response = self.client.post(... )

    # Assert
    self.assertEqual(response.status_code, 302)
```

## O que testar primeiro

- autorização e isolamento entre usuários;
- validações e invariantes importantes;
- casos de uso que alteram dados;
- queries/serviços com lógica real;
- bugs já encontrados — todo bug relevante deve ganhar teste de regressão.
> **ANTI-PADRÃO:** um teste que depende de internet, hora real, ordem de execução ou dados criados manualmente no seu banco local tende a ser frágil. Controle dependências e estado.

# 11. PostgreSQL e ORM: além do CRUD

O ORM evita SQL repetitivo, mas não elimina a necessidade de compreender banco relacional e custo de consultas.

## Conceitos a dominar

- chave primária e estrangeira
- NULL e defaults
- unique constraints
- índices
- transações
- joins
- N+1 queries
- concorrência básica e select_for_update em casos necessários
## N+1

```text
# Pode gerar uma query para Tasks + várias para Project
for task in Task.objects.all():
    print(task.project.name)

# Para ForeignKey, carregue junto quando fizer sentido
for task in Task.objects.select_related("project"):
    print(task.project.name)
```

Use select_related principalmente para relações single-valued como ForeignKey/OneToOne; prefetch_related é adequado para coleções/relações múltiplas. Otimize após entender a consulta, não por reflexo.

## Integridade no banco

Se uma regra é estrutural — por exemplo, um identificador deve ser único — prefira representá-la também como constraint no banco. Validação apenas na interface pode ser contornada por concorrência, scripts ou novas interfaces.

# 12. Boas práticas de código que valem mais que “arquitetura bonita”

Código sustentável é aquele cuja intenção fica clara e que permite mudanças previsíveis.

| Prática | Pergunta de revisão |
| --- | --- |
| nomes explícitos | entendo o que isso faz sem abrir cinco arquivos? |
| funções pequenas e coesas | a função tem um motivo principal para mudar? |
| dependências visíveis | de onde vêm banco, usuário e serviços externos? |
| queries centralizadas quando repetidas | a mesma regra de filtro está espalhada? |
| erros específicos | estou escondendo exceções com except Exception? |
| logs úteis | um erro em produção terá contexto suficiente? |
| sem abstração prematura | esta camada resolve um problema que já existe? |
| testabilidade | consigo validar a regra sem montar o sistema inteiro? |

## Ruff como guardrail

```bash
ruff check .
ruff check . --fix
ruff format .
ruff format --check .
```

Automatize estilo para não gastar energia de code review discutindo espaços, imports ou formatação. Reserve revisão humana para comportamento, arquitetura, segurança e legibilidade.

# 13. CI/CD: transforme boas intenções em regras automáticas

CI verifica a mudança continuamente. CD automatiza ou padroniza a entrega. Eles não substituem testes; eles garantem que testes e checks sejam realmente executados.

## Pipeline mínimo de CI

```text
Pull Request
   |
   +--> instalar dependências
   +--> ruff check
   +--> ruff format --check
   +--> django check
   +--> makemigrations --check --dry-run
   +--> testes contra PostgreSQL
   +--> build da image
   |
   +--> verde? merge permitido
```

## Exemplo conceitual de GitHub Actions

```yaml
name: CI
on: [push, pull_request]

jobs:
  test:
    runs-on: ubuntu-latest
    services:
      postgres:
        image: postgres:17
        env:
          POSTGRES_DB: taskflow_test
          POSTGRES_USER: postgres
          POSTGRES_PASSWORD: postgres
        ports: ["5432:5432"]
        options: >-
          --health-cmd pg_isready
          --health-interval 10s
          --health-timeout 5s
          --health-retries 5

    steps:
      - uses: actions/checkout@v6
      - uses: actions/setup-python@v6
        with:
          python-version: "3.13"
      - run: pip install -r requirements.txt
      - run: ruff check .
      - run: ruff format --check .
      - run: python manage.py check
      - run: python manage.py makemigrations --check --dry-run
      - run: python manage.py test
```

> **IDEIA CENTRAL:** se um requisito de qualidade é importante, tente torná-lo executável. “Lembre de rodar os testes” é mais fraco que “o PR não pode ser mergeado enquanto os testes falharem”.

# 14. Staging, produção e deploy

Deploy não é “copiar código para um servidor”. É promover uma versão conhecida através de um processo reproduzível.

## Fluxo ideal

```text
branch -> PR -> CI -> main -> build image -> staging -> smoke tests -> produção
                                  |                         |
                                  +------ mesma versão -----+
```

Uma prática forte é promover o mesmo artefato/imagem já validado em staging, mudando apenas configuração e segredos. Evite rebuilds diferentes e edições manuais no servidor.

## runserver não vai para produção

O servidor de desenvolvimento do Django não é adequado para produção. Em produção, use um servidor WSGI ou ASGI apropriado e deixe TLS/reverse proxy/load balancer de acordo com a plataforma escolhida.

## Checklist mínimo de produção

- [ ] DEBUG=False.
- [ ] SECRET_KEY única, longa e fora do repositório.
- [ ] ALLOWED_HOSTS correto.
- [ ] HTTPS habilitado; cookies de sessão/CSRF seguros quando aplicável.
- [ ] python manage.py check --deploy executado com settings de produção.
- [ ] static files coletados/servidos adequadamente.
- [ ] logs e error reporting configurados.
- [ ] backup do banco e restauração testada.
- [ ] healthcheck disponível.
- [ ] processo de rollback conhecido.
## Staging

Staging deve se parecer com produção em topologia e configuração de segurança, mas usar banco, credenciais, domínios e integrações separados. Dados reais só devem ser copiados quando houver justificativa e proteção/anonimização adequada.

# 15. Migrations, releases e rollback

Migrations são parte do deploy. Uma alteração de schema pode ser incompatível com a versão que ainda está atendendo tráfego.

## Expand / migrate / contract

| Etapa | Exemplo |
| --- | --- |
| Expand | adicionar display_name sem remover username |
| Migrate | preencher novos dados e fazer a aplicação escrever nos dois campos se necessário |
| Switch | nova versão passa a ler display_name |
| Contract | em release posterior, remover username quando já não for usado |

> **POR QUE:** deploys podem ter versões antiga e nova rodando simultaneamente por alguns instantes. Mudanças destrutivas imediatas tornam rollback e rolling deploy muito mais difíceis.

## Rollback

Rollback de código é simples quando você mantém imagens/tags anteriores. Rollback de banco é mais difícil: migrations destrutivas podem ter apagado dados. Por isso, prevenção e mudanças compatíveis valem mais que “ter um comando de rollback”.

# 16. Segurança básica que deve entrar desde o começo

Django oferece proteções úteis, mas configuração e autorização continuam sendo responsabilidade da aplicação.

| Risco | Prática |
| --- | --- |
| segredos expostos | variáveis/secret manager; nunca Git |
| Host header | ALLOWED_HOSTS |
| sessão em HTTP | HTTPS + SESSION_COOKIE_SECURE quando aplicável |
| CSRF | middleware/token do Django; não “desligar para funcionar” |
| SQL injection | ORM/queries parametrizadas; não montar SQL com strings |
| IDOR/autorização | filtrar objetos pelo usuário/tenant e testar acesso cruzado |
| dependências vulneráveis | atualizar e revisar dependências regularmente |
| dados sensíveis em logs | não registrar senhas/tokens/payloads desnecessários |

> **PRINCÍPIO:** autenticação responde “quem é?”. Autorização responde “pode fazer isso?”. Estar logado nunca deve ser tratado como permissão suficiente para acessar qualquer objeto.

# 17. Logs, healthchecks e observabilidade

Quando algo só falha em produção, prints aleatórios não são uma estratégia de diagnóstico.

## Logging

```python
import logging
logger = logging.getLogger(__name__)

logger.info("task_created", extra={"task_id": task.id, "user_id": request.user.id})
```

O formato exato depende da infraestrutura, mas mantenha contexto útil e evite dados sensíveis. Em sistemas maiores, logs estruturados facilitam busca e correlação.

## Healthcheck

```text
GET /health/ -> 200 {"status": "ok"}
```

Diferencie readiness (a aplicação está pronta para receber tráfego?) de liveness (o processo está vivo?). Para o primeiro projeto, um endpoint simples já introduz a ideia; depois você pode testar dependências críticas com cuidado.

## O próximo nível

- error tracking (ex.: Sentry ou equivalente)
- métricas de latência, erro e throughput
- tracing distribuído
- alertas baseados em sintomas do usuário
# 18. Checklists de referência

Use estas listas antes de cada PR e antes de cada release até que o processo vire hábito.

## Antes de abrir PR

- [ ] branch tem escopo claro
- [ ] código formatado
- [ ] Ruff passa
- [ ] tests passam
- [ ] migration necessária foi criada
- [ ] nenhum segredo/arquivo local entrou no diff
- [ ] README/documentação alterados se necessário
- [ ] você leu o diff completo
## Antes de merge

- [ ] CI verde
- [ ] revisão concluída
- [ ] mudança é compatível com o schema atual
- [ ] impacto de permissão foi avaliado
- [ ] não há TODO crítico escondendo comportamento incompleto
## Antes de produção

- [ ] tag/release identificável
- [ ] imagem/artefato já validado em staging
- [ ] backup e rollback entendidos
- [ ] migrations revisadas
- [ ] check --deploy verde
- [ ] static files preparados
- [ ] variáveis de produção presentes
- [ ] healthcheck e logs verificados
- [ ] smoke test definido
# 19. Folha de comandos

Não memorize tudo. Memorize o papel de cada grupo e use esta página como referência.

## Django

```bash
django-admin startproject config .
python manage.py startapp tasks
python manage.py runserver
python manage.py makemigrations
python manage.py migrate
python manage.py makemigrations --check --dry-run
python manage.py shell
python manage.py test
python manage.py check
python manage.py check --deploy --settings=config.settings.production
python manage.py collectstatic --noinput
```

## Git

```bash
git status
git switch -c feat/minha-feature
git add -p
git commit -m "feat: add ..."
git push -u origin feat/minha-feature
git log --oneline --graph --decorate
```

## Docker

```bash
docker build -t taskflow:dev .
docker run --rm taskflow:dev
docker compose up --build
docker compose up -d
docker compose ps
docker compose logs -f web
docker compose exec web python manage.py migrate
docker compose down
docker compose down -v
```

## Qualidade

```bash
ruff check .
ruff check . --fix
ruff format .
ruff format --check .
```

# 20. O que estudar depois dos 10 dias

Depois da base, aumente profundidade sem trocar de assunto a cada dia.

| Ordem | Tema | Objetivo |
| --- | --- | --- |
| 1 | Django REST Framework | APIs, serializers, permissions e pagination |
| 2 | PostgreSQL mais profundo | EXPLAIN, índices, locks, transações |
| 3 | Docker produção | multi-stage, usuários não-root, cache de build |
| 4 | Redis + caching | cache consciente, sessões, rate limiting conforme caso |
| 5 | Celery/filas | tarefas assíncronas e retries |
| 6 | Observabilidade | logs estruturados, métricas, tracing |
| 7 | Deploy/cloud | DNS, TLS, networking, storage, autoscaling |
| 8 | Arquitetura avançada | DDD/CQRS apenas onde o problema justificar |

> **ORDEM IMPORTA:** não use microservices, Kafka, Kubernetes, CQRS ou event sourcing para “parecer backend profissional”. O profissional é quem consegue explicar o custo e o benefício e escolher não usar quando não precisa.

# 21. Perguntas que você deve saber responder

Se você consegue responder estas perguntas com exemplos do TaskFlow, sua base já está muito mais sólida.

- [ ] O que acontece no Django do momento em que chega um GET até a resposta?
- [ ] Qual a diferença entre project e app?
- [ ] O que uma migration representa? Por que ela entra no Git?
- [ ] Qual a diferença entre select_related e prefetch_related?
- [ ] Por que não devo usar SQLite local se quero testar comportamento específico de PostgreSQL?
- [ ] Authentication e authorization são a mesma coisa?
- [ ] Quando você criaria um service.py e quando não criaria?
- [ ] O que o Docker resolve que um venv não resolve?
- [ ] Qual a diferença entre image, container e volume?
- [ ] Por que localhost não aponta para o PostgreSQL em outro container?
- [ ] Qual a diferença entre CI e CD?
- [ ] Por que staging deve usar segredos e banco diferentes de produção?
- [ ] Por que runserver não deve ser usado em produção?
- [ ] Como você impediria uma migration de quebrar uma versão antiga ainda rodando?
- [ ] Como você faria rollback de uma release?
- [ ] Quais checks você colocaria como obrigatórios antes de merge?

# Referências oficiais

Use documentação oficial como fonte principal. Tutoriais são úteis para exemplos; a documentação deve ser a referência para comportamento e versão.

- [Django 6.1 — documentação](https://docs.djangoproject.com/pt-br/6.1/)
- [Django — instalação e versões de Python](https://docs.djangoproject.com/en/6.1/faq/install/)
- [Django — testes](https://docs.djangoproject.com/pt-br/6.1/intro/tutorial05/)
- [Django — ferramentas de testes](https://docs.djangoproject.com/en/6.1/topics/testing/tools/)
- [Django — deploy](https://docs.djangoproject.com/pt-br/6.1/howto/deployment/)
- [Django — deployment checklist](https://docs.djangoproject.com/en/6.1/howto/deployment/checklist/)
- [Django — segurança](https://docs.djangoproject.com/pt-br/6.1/topics/security/)
- [Django — static files](https://docs.djangoproject.com/en/6.1/ref/contrib/staticfiles/)
- [Docker — Compose](https://docs.docker.com/compose/)
- [Docker — Compose quickstart](https://docs.docker.com/compose/gettingstarted/)
- [Docker — build best practices](https://docs.docker.com/build/building/best-practices/)
- [GitHub — branches](https://docs.github.com/en/pull-requests/reference/branches)
- [GitHub — pull requests](https://docs.github.com/en/pull-requests)
- [GitHub Actions — PostgreSQL service containers](https://docs.github.com/en/actions/tutorials/use-containerized-services/create-postgresql-service-containers)
- [Ruff — formatter](https://docs.astral.sh/ruff/formatter/)
- [OpenAI — Codex e AGENTS.md](https://openai.com/index/introducing-codex/)
- [OpenAI — Codex, code review e CLI](https://openai.com/index/introducing-upgrades-to-codex/)

# Regra final

> **NÃO ESTUDE PARA DECORAR DJANGO. ESTUDE PARA CONSEGUIR TOMAR DECISÕES.**

O framework muda. O modelo mental de HTTP, dados, testes, isolamento, versionamento e entrega continua útil.

Primeiro objetivo prático: complete o Dia 1 sem copiar uma solução pronta. Depois, use o próprio projeto como laboratório para todos os dias seguintes.
