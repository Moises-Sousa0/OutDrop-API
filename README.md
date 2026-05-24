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
- `PUT /lancamentos/{id}` — protegida
- `DELETE /lancamentos/{id}` — protegida

### Outros
- `GET /health`

## Próximos passos


- Swagger documentado
- Deploy

## VARIAVEIS DO AMBIENTE
```
Crie um arquivo `.env` na raiz do projeto com as seguintes variáveis:

DATABASE_URL=postgresql://usuario:senha@localhost/nome_do_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
```

## COMO RODAR LOCALMENTE

1. Clone o repositório
2. Crie e ative o ambiente virtual:
    python -m venv venv
    venv\Scripts\activate
3. Instale as dependências:
    pip install -r requirements.txt
4. Configura o arquivo .env com as variaveis do ambiente
5. Rode o servidor:
    uvicorn app.main:app --reload
6. Acesse a documentação em http://127.0.0.1:8000/docs
