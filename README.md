# OUTDROP API
API para gerenciamento de drops de marcas de roupas - sendo possível cadastrar marcas, produtos e lançamentos.


## Tecnologias
- Python
- FastAPI
- PostgreSQL 
- SQLAlchemy & psycopg2
- Pydantic
- Passlib (com Bcrypt) & Python-Jose (JWT)
- Python-dotenv

## Rotas disponiveis
- GET /health
- POST /marcas
- GET /marcas
- GET /marcas/{id}
- PUT /marcas/{id}
- DELETE /marcas/{id}
- POST /produtos
- GET /produtos
- GET /produtos/{id}
- PUT /produtos/{id}
- DELETE /produtos/{id}
- POST /usuarios
- POST /login

## Próximos passos
- Implementar a função verificar_token 
- Proteger rotas que exigem autenticação 
- Relacionamentos e autorização
- Tratamento de erros
- Deploy 

