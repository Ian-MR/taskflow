# Learning Progress — TaskFlow

> Atualize este arquivo no fim de cada sessão. Ele existe para o Codex entender seu estágio sem assumir que uma feature pronta significa que o conceito foi aprendido.

## Estado atual

- **Dia atual:** 7
- **Branch atual:** `feat/orm-ci`
- **Objetivo da sessão:** performance ORM, integração contínua e proteção da main
- **Última PR revisada:** `feat/orm-ci — APPROVE`
- **Tema que mais preciso reforçar:** escolher entre select_related, prefetch_related e annotate

## Dia 1 — HTTP, project/app, URLs, views e Git

- [x] Consigo explicar `request → URLconf → view → response` sem consultar.
- [x] Consigo recriar o projeto e a venv em uma pasta vazia.
- [x] Sei explicar working tree, staging area, commit e branch.
- [x] `.venv` e `.env` não são versionados.

**O que implementei:**
Inciei um projeto com django, aprendi sobre a estrutura d projeto, criei views e configurei os path da url
**O que aprendi:**
Como funciona a estrutura em um projeto com django, e os comando importans pra trabalhar no projeto
**Dúvidas/buracos:**
ainda esqueco um pouco os comandos, e tenho um pouco de duvida como comentar corretamente o commit
**Feedback da revisão:**
- manter o nome da view consistente com o URLconf;
- importar classes antes de usá-las;
- HttpResponse é instanciado, não possui .send();
- aliases evitam colisão entre módulos chamados views;
- commit registra a staging area no histórico.

---

## Dia 2 — Models, migrations, ORM e PostgreSQL

- [x] Sei explicar classe Model → migration → schema.
- [x] Sei quando usar `ForeignKey` e `ManyToManyField`.
- [x] Entendo QuerySet lazy.
- [x] Sei explicar por que migration entra no Git.

**Notas:**
- Project e Task com ForeignKey;
- migrations 0001 e 0002;
- diferença entre makemigrations e migrate;
- QuerySet lazy;
- choices versus CheckConstraint;
- PostgreSQL 18.6 e autenticação SCRAM;
- risco de duplicação dos valores de status.

---

## Dia 3 — Forms, templates e configuração

- [x] Validação importante existe no backend.
- [x] Consigo explicar template inheritance.
- [x] Nenhum segredo está no Git.
- [x] Sei diferenciar configuração local e production.

**Notas:**
- template inheritance com `base.html`;
- context conecta dados da view ao template;
- ModelForm valida criação e edição;
- `instance=project` diferencia update de insert;
- `.env` guarda valores locais e `.env.example` documenta as variáveis;
- `SECRET_KEY` foi rotacionada e movida para o ambiente.

---

## Dia 4 — Auth, autorização e Pull Request

- [x] Sei diferenciar authentication de authorization.
- [x] Tenho teste de acesso cruzado entre usuários.
- [x] Trabalho em branch e reviso meu próprio diff.
- [x] A PR passou por review do Codex em modo sênior.

**Notas:**
- authentication comprovada pelo redirect de usuário anônimo;
- autorização comprovada manualmente: user_a não acessa o projeto 3 e user_b não acessa o projeto 2;
- `owner` permanece nullable durante a fase de expansão, até existir um backfill reproduzível;
- revisão local feita contra `main`, pois ainda não existe remoto configurado.

---

## Dia 5 — Código sustentável e Ruff

- [x] Ruff passa.
- [x] Consigo justificar QuerySet/Manager/service usados.
- [x] Removi duplicação real sem abstração prematura.
- [x] Consigo apontar um trade-off da minha estrutura atual.

**Notas:**
- Ruff configurado como linter e formatter;
- pre-commit executa Ruff antes de commits com arquivos Python;
- `ProjectQuerySet.owned_by()` centraliza a consulta por owner;
- views atuais permanecem pequenas; não foi criado service sem necessidade;
- trade-off: `owned_by()` facilita uso seguro, mas não impede consultas que esqueçam o escopo do owner.

---

## Dia 6 — Testes

- [x] Testes são independentes e determinísticos.
- [x] Tenho testes de permissão e validação.
- [x] Sei explicar Arrange–Act–Assert.
- [x] Um bug relevante ganhou teste de regressão.

**Notas:**
- suíte com 6 testes executada também em ordem aleatória;
- `TestCase` usa banco isolado e cada teste prepara seus próprios dados;
- criação válida, formulário inválido, usuário anônimo e acesso entre owners estão protegidos;
- `refresh_from_db()` confirma o estado realmente persistido;
- role PostgreSQL local recebeu `CREATEDB` para criar o banco de teste; produção não deve receber essa permissão.

---

## Dia 7 — ORM eficiente e CI

- [x] Sei reconhecer N+1.
- [x] Sei diferenciar `select_related` de `prefetch_related`.
- [x] CI executa checks/testes.
- [x] Sei explicar CI versus CD.

**Notas:**
- N+1 reproduzido com 5 queries onde eram esperadas 3;
- `annotate(Count("tasks"))` mantém a listagem em 3 queries;
- `LEFT OUTER JOIN` preserva projetos com zero tarefas;
- `select_related` atende relações únicas e `prefetch_related` atende coleções;
- GitHub Actions executa Ruff, Django checks, migrations check e 7 testes no PostgreSQL 18.6;
- branch `main` exige PR e o status check `checks` verde;
- CI valida mudanças; CD entrega ou implanta o código depois dos checks.

---

## Dia 8 — Docker / Compose

- [ ] Sei explicar image, container, layer e Dockerfile.
- [ ] Sei explicar volume versus bind mount.
- [ ] Entendo networking do Compose e por que `localhost` costuma estar errado entre containers.
- [ ] `docker compose up` inicia app + PostgreSQL.
- [ ] Sei dizer quais dados sobrevivem a `docker compose down`.

**Notas:**

---

## Dia 9 — Staging e produção

- [ ] Sei explicar `DEBUG`, `ALLOWED_HOSTS` e secrets.
- [ ] Sei por que `runserver` não é servidor de produção.
- [ ] `check --deploy` foi entendido/executado.
- [ ] Sei diferenciar local, test, staging e production.

**Notas:**

---

## Dia 10 — Release, migration e rollback

- [ ] Sei explicar artefato imutável.
- [ ] Criei uma tag de release.
- [ ] Entendo expand/migrate/switch/contract.
- [ ] Sei explicar estratégia de rollback e seus limites com banco.
- [ ] README permite outra pessoa iniciar o projeto.
- [ ] PR/release final recebeu review sênior.

**Notas:**

---

## Registro de bugs

| Data | Sintoma | Causa-raiz | Como diagnostiquei | Teste de regressão? |
|---|---|---|---|---|
| | | | | |

## Decisões de arquitetura

| Decisão | Alternativas consideradas | Por que escolhi | Quando reavaliar |
|---|---|---|---|
| | | | |

## Findings recorrentes de PR review

| Tema | Ocorrências | O que vou fazer diferente |
|---|---:|---|
| | | |
