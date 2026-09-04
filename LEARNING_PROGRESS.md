# Learning Progress — TaskFlow

> Atualize este arquivo no fim de cada sessão. Ele existe para o Codex entender seu estágio sem assumir que uma feature pronta significa que o conceito foi aprendido.

## Estado atual

- **Dia atual:** 2
- **Branch atual:** `main`
- **Objetivo da sessão:** models, migrations, ORM e PostgreSQL;
- **Última PR revisada:** nenhuma
- **Tema que mais preciso reforçar:** comandos de criação e mensagens de commit

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

- [ ] Validação importante existe no backend.
- [ ] Consigo explicar template inheritance.
- [ ] Nenhum segredo está no Git.
- [ ] Sei diferenciar configuração local e production.

**Notas:**

---

## Dia 4 — Auth, autorização e Pull Request

- [ ] Sei diferenciar authentication de authorization.
- [ ] Tenho teste de acesso cruzado entre usuários.
- [ ] Trabalho em branch e reviso meu próprio diff.
- [ ] A PR passou por review do Codex em modo sênior.

**Notas:**

---

## Dia 5 — Código sustentável e Ruff

- [ ] Ruff passa.
- [ ] Consigo justificar QuerySet/Manager/service usados.
- [ ] Removi duplicação real sem abstração prematura.
- [ ] Consigo apontar um trade-off da minha estrutura atual.

**Notas:**

---

## Dia 6 — Testes

- [ ] Testes são independentes e determinísticos.
- [ ] Tenho testes de permissão e validação.
- [ ] Sei explicar Arrange–Act–Assert.
- [ ] Um bug relevante ganhou teste de regressão.

**Notas:**

---

## Dia 7 — ORM eficiente e CI

- [ ] Sei reconhecer N+1.
- [ ] Sei diferenciar `select_related` de `prefetch_related`.
- [ ] CI executa checks/testes.
- [ ] Sei explicar CI versus CD.

**Notas:**

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
