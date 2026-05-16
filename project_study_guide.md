# PROJETO

Uma API completa de gestão de despesas partilhadas. Os utilizadores registam-se, criam grupos, adicionam despesas e o sistema calcula automaticamente quem deve quanto a quem. Tudo protegido por autenticação real.

## STACKS A USAR E PARA QUE SERVEM

### FastAPI

É o framework web em Python. É ele que recebe os pedidos HTTP (GET, POST, etc.), valida os dados de entrada e devolve as respostas. Escolhi FastAPI porque gera documentação Swagger automaticamente, é extremamente rápido e usa type hints do Python nativo


### PostgreSQL

É a base de dados relacional onde tudo fica guardado — utilizadores, grupos, despesas, pagamentos. Escolhi PostgreSQL em vez de SQLite porque é o que se usa em produção em empresas reais, suporta transações ACID e é robusto


##### NOTA:

Transações ACID - são um conjunto de quatro propriedades fundamentais (Indivisibilidade, Consistência, Isolamento e Durabilidade) que garantem a integridade, a segurança e a precisão dos dados


### SQLAlchemy

É o ORM (Object Relational Mapper). Em vez de escrever SQL puro, defino os meus modelos como classes Python e o SQLAlchemy traduz para SQL. Também gere a ligação à base de dados


### Alembic

Gere as migrações da base de dados. Quando mudo o schema (adicionar uma coluna, por exemplo), o Alembic cria um ficheiro de migração que atualiza a base de dados sem perder dados


### JWT

(JSON Web Tokens)
É o mecanismo de autenticação. Quando alguem faz login recebo um token. Nas chamadas seguintes envio esse token no header e a API sabe quem é sem precisar de ir à base de dados verificar a password. O token tem expiração e existe um refresh token para renovar sem fazer login de novo.


### Redis

Base de dados em memória, extremamente rápida. pretendo usá-la para duas coisas: guardar refresh tokens invalidados (logout real) e fazer rate limiting (limitar o número de pedidos por IP para evitar ataques)


### Docker + Docker Compose

Empacota a aplicação inteira em containers. Com um único comando `docker-compose up` qualquer pessoa levanta o PostgreSQL, o Redis e a API sem instalar nada manualmente


### Pydantic

Define os schemas dos dados de entrada e saída. Se alguém enviar um email inválido ou um campo a mais, o Pydantic rejeita automaticamente antes de chegar à lógica da aplicação


##### NOTA

feat:     adicionei novas funcionalidades
fix:      dei fix a um bug que estava a acontecer
refactor: mudei a estrutura do codigo sem mudar o comportamento da app
docs:     alterei apenas a documetacao - se mudar a logica da app

## COMO TUDO SE LIGA

```text
Cliente (Postman / Frontend)
        ↓ HTTP Request
    FastAPI  ←→  Pydantic (valida dados)
        ↓
    SQLAlchemy  ←→  PostgreSQL (dados persistentes)
        ↓
      Redis (tokens + rate limiting)
        ↓
    JWT (autenticação em cada pedido)
```
