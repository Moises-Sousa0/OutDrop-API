# OUTDROP API

API para gerenciamento de drops de marcas de roupas — sendo possível cadastrar marcas, produtos e lançamentos.

## Tecnologias

- Python
- FastAPI
- PostgreSQL
- SQLAlchemy & psycopg2
- Pydantic
- Passlib (com Bcrypt) & Python-Jose (JWT)
- Python-dotenv

## Rotas disponíveis

### Marcas
- `POST /marcas` — protegida
- `GET /marcas`
- `GET /marcas/{id}`
- `PUT /marcas/{id}` — protegida
- `DELETE /marcas/{id}` — protegida

### Produtos
- `POST /produtos` — protegida
- `GET /produtos`
- `GET /produtos/{id}`
- `PUT /produtos/{id}` — protegida
- `DELETE /produtos/{id}` — protegida

### Usuários
- `POST /usuarios`
- `POST /login`
- `GET /usuarios/me` — protegida
- `PUT /usuarios/me` — protegida

### Lançamentos
- `POST /lancamentos` — protegida
- `GET /lancamentos`
- `GET /lancamentos/{id}`

### Outros
- `GET /health`

## Próximos passos

- DELETE e PUT de lançamentos
- Tratamento de erros global
- Swagger documentado
- Deploy
