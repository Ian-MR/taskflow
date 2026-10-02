# ADR-0001 — Retirar o domínio legado TaskFlow

**Status:** Accepted

**Date:** 2026-10-02

## Context

O repositório está migrando do TaskFlow para um Personal Finance Manager.

Os models Project e Task pertenciam exclusivamente à Fase 1 e não possuem significado no novo domínio financeiro. Os dados existentes eram sintéticos, foram usados somente para aprendizado e não precisavam ser preservados.

A autenticação, os usuários e a infraestrutura construída na Fase 1 continuam úteis para o novo produto.

## Decision

Remover definitivamente o domínio Project/Task da aplicação.

As rotas, views, forms, templates, testes e models do TaskFlow serão removidos. As tabelas correspondentes serão excluídas pela migration `0006`.

Usuários e autenticação serão preservados.

O app `projects` permanecerá temporariamente instalado como um esqueleto, contendo seu histórico de migrations, até que a migration de remoção tenha sido aplicada em todos os ambientes.

O código da Fase 1 permanece preservado pela tag `v0.1.0`.

## Alternatives considered

### Manter o TaskFlow isolado

**Vantagens:**

- permitiria reativar as funcionalidades antigas rapidamente;
- manteria os dados existentes acessíveis.

**Desvantagens:**

- manteria código sem utilidade para o novo produto;
- aumentaria a manutenção e a complexidade da aplicação.

### Usar uma feature flag

**Vantagens:**

- permitiria habilitar ou desabilitar o domínio sem novo deploy.

**Desvantagens:**

- introduziria configuração e caminhos de execução desnecessários;
- não existe requisito de produto para reativar o TaskFlow.

### Remover definitivamente por migration

**Vantagens:**

- deixa o projeto focado no novo domínio;
- mantém a evolução do schema reproduzível;
- exercita uma transição compatível com bancos existentes.

**Desvantagens:**

- apaga permanentemente os dados de Project e Task;
- um rollback da migration recria a estrutura, mas não recupera os registros.

## Consequences

### Positive

- o domínio antigo deixa de interferir no desenvolvimento financeiro;
- usuários, autenticação, CI e infraestrutura são preservados;
- bancos existentes e bancos novos chegam ao mesmo schema final.

### Negative / trade-offs

- os dados legados são perdidos;
- a tag `v0.1.0` preserva o código, mas não os dados apagados;
- o app `projects` precisa permanecer temporariamente para carregar as migrations.

## Revisit when

Depois que a migration `0006` tiver sido aplicada em todos os ambientes, avaliar a remoção definitiva do esqueleto do app `projects`.
