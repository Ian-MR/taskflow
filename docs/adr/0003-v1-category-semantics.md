# ADR-0003 — Definir a semântica das categorias da V1

**Status:** Accepted

**Date:** 2026-10-02

## Context

A V1 precisa permitir que usuários organizem receitas e despesas usando categorias privadas.

As regras precisam impedir acesso entre usuários, evitar categorias duplicadas e preservar transações quando uma categoria for removida.

A categoria deve continuar opcional, conforme definido no ADR-0002.

## Decision

Cada categoria pertencerá obrigatoriamente a um usuário.

Categorias serão privadas. Um usuário não poderá visualizar, alterar, excluir ou utilizar categorias pertencentes a outro usuário.

Cada categoria terá um tipo fixo:

- `income` para receitas;
- `expense` para despesas.

Uma transação somente poderá utilizar uma categoria que pertença ao mesmo usuário e tenha o mesmo tipo da transação.

O nome será obrigatório. Espaços no início e no final serão removidos antes da validação. Um nome que fique vazio depois dessa normalização será inválido.

A unicidade do nome será verificada dentro da combinação owner e tipo, sem diferenciar letras maiúsculas e minúsculas.

Como consequência:

- `Salário` e `salário` serão duplicados para o mesmo usuário e tipo;
- o mesmo usuário poderá usar o mesmo nome em tipos diferentes;
- usuários diferentes poderão usar o mesmo nome;
- acentos continuarão significativos.

Serão inválidos:

- categoria sem owner;
- nome vazio depois da remoção dos espaços externos;
- tipo diferente de `income` ou `expense`;
- nome duplicado para o mesmo owner e tipo, ignorando maiúsculas e minúsculas;
- transação associada a uma categoria de outro usuário;
- transação associada a uma categoria de tipo incompatível.

A categoria será opcional em uma transação. Quando não houver categoria, a interface apresentará "Sem categoria". Esse texto não representará um registro automático no banco.

Categorias poderão ser excluídas definitivamente. A exclusão de uma categoria não excluirá suas transações. As transações relacionadas passarão a ficar sem categoria.

Depois da exclusão, o mesmo usuário poderá criar outra categoria com o mesmo nome e tipo.

A V1 não terá arquivamento de categorias, categorias globais, cores, ícones ou categorização automática.

## Alternatives considered

### Permitir uma categoria para receitas e despesas

Uma categoria sem tipo reduziria a quantidade de registros e poderia ser
reutilizada em qualquer transação.

Essa alternativa foi rejeitada porque receitas e despesas possuem significados
diferentes. Um tipo fixo torna a seleção e a validação mais explícitas.

### Tornar o nome único somente por usuário

Essa alternativa impediria o mesmo usuário de utilizar um nome em uma categoria
de receita e em outra de despesa.

Ela foi rejeitada porque os tipos possuem conjuntos separados de categorias.
A unicidade por owner e tipo preserva essa separação.

### Exigir categoria em todas as transações

Essa alternativa garantiria que todos os lançamentos fossem classificados.

Ela foi rejeitada porque obrigaria o usuário a criar uma categoria antes de
registrar uma transação. A V1 permite lançamentos sem categoria e os apresenta
como “Sem categoria”.

### Criar automaticamente uma categoria “Sem categoria”

Essa alternativa evitaria valores nulos na relação entre transação e categoria.

Ela foi rejeitada porque exigiria criar e manter um registro automático para
cada usuário. A ausência de categoria já representa esse estado sem adicionar
dados artificiais.

### Arquivar categorias

Uma categoria arquivada poderia permanecer associada às transações antigas e
deixar de aparecer para novos lançamentos.

Essa alternativa foi rejeitada porque adicionaria status e regras de filtragem
sem necessidade atual de auditoria. Na V1, a categoria será excluída e a
transação será preservada sem categoria.

### Criar categorias iniciais automaticamente

Um conjunto de categorias comuns poderia ser criado para cada usuário.

Essa alternativa foi adiada porque exigiria definir provisionamento, idempotência, comportamento para usuários existentes e conflitos com categorias já criadas. Ela poderá ser reavaliada depois que o CRUD básico de categorias estiver funcionando.

## Consequences

### Positive

- categorias ficam isoladas por usuário;
- receitas e despesas possuem conjuntos separados de categorias;
- nomes duplicados são tratados de forma previsível;
- transações podem ser registradas sem categoria;
- excluir uma categoria não apaga histórico financeiro;
- a V1 não precisa manter categorias automáticas ou arquivadas.

### Negative / trade-offs

- excluir uma categoria remove sua classificação das transações antigas;
- a associação anterior não poderá ser recuperada sem backup;
- o mesmo texto pode existir duas vezes para um usuário quando os tipos forem
  diferentes;
- mudanças futuras de tipo exigirão uma regra explícita para transações já
  associadas.

## Revisit when

Esta decisão deverá ser revisada antes de:

- exigir histórico de classificação ou auditoria;
- permitir arquivamento de categorias;
- introduzir categorias globais ou compartilhadas;
- permitir alteração do tipo de uma categoria já utilizada;
- implementar categorização automática;
- importar transações de fontes externas;
- oferecer categorias iniciais opcionais;
- adicionar cores ou ícones às categorias.
