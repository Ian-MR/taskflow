# ADR-0002 — Definir a semântica das transações da V1

**Status:** Accepted

**Date:** 2026-10-02

## Context

A V1 precisa representar receitas e despesas de maneira inequívoca para
calcular entradas, saídas e resultado por período.

As regras devem evitar valores monetários ambíguos, erros de precisão e
confusão entre a data em que uma transação pertence ao relatório e a data em
que o registro foi criado.

A modelagem deve atender ao Personal Expense Manager sem antecipar contas,
cartões, estornos, auditoria ou suporte a múltiplas moedas.

## Decision

O valor monetário será armazenado em `amount` como uma magnitude sempre
positiva. Zero e valores negativos serão inválidos.

O valor terá duas casas decimais e capacidade máxima de `9.999.999,99`.

O campo `type` determinará o efeito financeiro da transação:

- `income` aumenta o resultado do período;
- `expense` reduz o resultado do período.

Todas as transações da V1 serão interpretadas como valores em BRL. Não haverá
uma coluna de moeda enquanto o produto não suportar outras moedas de forma
completa.

A data financeira será obrigatória, editável e usada para determinar o período
dos relatórios. Seu valor inicial será a data local em
`America/Sao_Paulo`. O campo `created_at` registrará quando o objeto foi criado,
mas não determinará o período financeiro.

A categoria será opcional. Quando não houver categoria, a interface apresentará
a transação como “Sem categoria”, sem criar uma categoria automática no banco.

Owner, descrição, tipo, valor e data financeira serão obrigatórios. Notas serão
opcionais.

A V1 permitirá editar e excluir definitivamente uma transação criada por
engano. Não haverá status de cancelamento nem implementação formal de estornos.

## Alternatives considered

### Armazenar o valor com sinal

O sinal poderia representar diretamente o efeito financeiro: positivo para
receita e negativo para despesa.

Essa alternativa foi rejeitada porque permitiria combinações ambíguas entre
sinal e tipo. Manter o valor positivo e o tipo separado torna a validação e a
leitura do domínio mais explícitas.

### Armazenar uma coluna de moeda

Uma coluna permitiria registrar códigos como BRL ou USD desde o início.

Essa alternativa foi rejeitada porque uma coluna não resolve conversão,
cotação ou soma de valores em moedas diferentes. Como toda a V1 utiliza BRL, o
campo não teria variação real. O suporte multimoeda exigirá uma nova decisão de
domínio.

### Manter transações canceladas

Um status de cancelamento preservaria o registro para auditoria e permitiria
excluí-lo dos totais sem removê-lo do banco.

Essa alternativa foi rejeitada porque a V1 ainda utiliza dados sintéticos e
não possui requisito de auditoria. Introduzir status também exigiria regras de
cancelamento e reativação sem uma necessidade atual.

## Consequences

### Positive

- receitas e despesas possuem semântica explícita;
- valores inválidos podem ser rejeitados de forma consistente;
- os totais não dependem do sinal armazenado;
- a data financeira fica separada da data de criação;
- transações podem existir sem categoria;
- a V1 permanece limitada ao domínio necessário atualmente.

### Negative / trade-offs

- exclusões são permanentes;
- não existe histórico de cancelamento;
- estornos não possuem representação própria;
- valores em outras moedas não são suportados;
- a capacidade monetária precisará ser revista caso deixe de atender ao produto.

## Revisit when

Esta decisão deverá ser revisada antes de:

- utilizar dados financeiros reais;
- exigir auditoria ou histórico imutável;
- implementar cancelamentos ou estornos;
- introduzir contas ou cartões;
- suportar múltiplas moedas;
- aceitar valores acima da capacidade definida.
