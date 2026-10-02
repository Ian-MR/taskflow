# Política de tratamento de dados financeiros

## Objetivo

Esta política define como dados financeiros, dados pessoais, credenciais e
artefatos relacionados devem ser tratados durante o desenvolvimento e a
operação do Personal Finance Manager.

Até que o projeto alcance explicitamente um marco de prontidão para produção,
todos os ambientes devem utilizar somente dados sintéticos.

## Dados sensíveis

São considerados sensíveis:

- descrições, valores e datas de transações reais;
- saldos e informações de contas;
- números de conta, agência, cartão ou documentos;
- nomes, e-mails e outros dados pessoais;
- arquivos CSV, OFX ou QFX obtidos de instituições financeiras;
- dumps e backups de bancos com dados reais;
- senhas, tokens, chaves privadas e credenciais;
- logs ou screenshots que exponham essas informações.

## Política por ambiente

| Ambiente | Dados permitidos |
| --- | --- |
| Desenvolvimento | Somente dados sintéticos |
| Testes automatizados | Somente dados sintéticos |
| Staging | Somente dados sintéticos |
| Produção | Dados reais somente após revisão de prontidão |
| Repositório Git | Nenhum dado financeiro real ou segredo |

Dados de produção não podem ser copiados para desenvolvimento, testes ou
staging.

## Dados sintéticos

Dados sintéticos devem ser fictícios e não podem ser derivados de transações,
contas ou pessoas reais.

Fixtures, exemplos, screenshots e demonstrações devem utilizar nomes, valores,
descrições e identificadores inventados.

## Uso de dados reais

Dados financeiros reais somente poderão entrar no sistema por meio da aplicação
em um ambiente de produção aprovado.

Dados reais não devem ser inseridos diretamente no código, em fixtures,
migrations, scripts versionados ou arquivos incluídos no repositório.

Antes do primeiro uso de dados reais, deve ser realizada uma revisão de
segurança e backup que confirme:

- HTTPS configurado;
- autenticação e autorização validadas;
- isolamento de dados entre usuários testado;
- segredos fornecidos por variáveis de ambiente;
- banco de produção isolado dos demais ambientes;
- backup configurado e protegido;
- procedimento de restauração testado;
- logs sem dados financeiros sensíveis;
- procedimento de resposta a incidentes definido.

A autorização para uso de dados reais deve ser registrada explicitamente na
documentação do projeto.

## Arquivos proibidos no Git

Nunca devem ser adicionados ao repositório:

- arquivos `.env` com valores reais;
- exports bancários CSV, OFX ou QFX;
- dumps SQL ou backups de banco;
- tokens de acesso ou atualização;
- senhas e credenciais;
- chaves privadas ou certificados privados;
- screenshots contendo dados reais;
- logs contendo informações financeiras ou pessoais;
- credenciais de Open Finance.

O `.gitignore` funciona como proteção adicional, mas não substitui a revisão do
conteúdo antes do commit.

## Logs e screenshots

Logs devem registrar somente informações necessárias para diagnóstico.

Descrições financeiras, valores, tokens, senhas e dados bancários não devem ser
registrados.

Screenshots usados em issues, PRs ou documentação devem conter dados sintéticos
ou estar completamente anonimizados.

## Revisão antes do commit

Antes de cada commit relacionado a dados ou configuração, o desenvolvedor deve
verificar:

- arquivos staged;
- presença de exports ou dumps;
- presença de `.env` ou credenciais;
- conteúdo de fixtures e exemplos;
- logs e screenshots adicionados.

Arquivos ignorados pelo Git ainda devem ser armazenados e descartados com
cuidado.

## Exposição acidental

Se um segredo for commitado, ele deve ser considerado comprometido mesmo que o
commit ainda não tenha sido enviado ao repositório remoto.

Nesse caso:

1. interromper o compartilhamento ou deploy;
2. revogar ou rotacionar o segredo;
3. identificar onde ele foi exposto;
4. remover o dado do histórico quando necessário;
5. verificar logs e acessos relacionados;
6. registrar o incidente e a ação corretiva.

Se dados financeiros reais forem expostos:

1. interromper o acesso ao dado;
2. preservar as informações necessárias para investigar;
3. identificar quais dados e usuários foram afetados;
4. revisar credenciais, permissões e backups;
5. definir a ação de recuperação antes de continuar a operação.

Apagar somente o arquivo mais recente não elimina seu conteúdo do histórico do
Git.

## Revisão desta política

Esta política deve ser revisada antes de:

- utilizar dados financeiros reais;
- implementar importação CSV ou OFX;
- integrar com Open Finance;
- armazenar informações de contas ou cartões;
- disponibilizar a aplicação para outros usuários;
- alterar a estratégia de backup ou hospedagem.
