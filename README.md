OUTDROP API
API para gerenciamento de drops de marcas de roupas — sendo possível cadastrar marcas, produtos e lançamentos.
Tecnologias

Python
FastAPI
PostgreSQL
SQLAlchemy & psycopg2
Pydantic
Passlib (com Bcrypt) & Python-Jose (JWT)
Python-dotenv

Rotas disponíveis

GET /health
POST /marcas — protegida
GET /marcas
GET /marcas/{id}
PUT /marcas/{id} — protegida
DELETE /marcas/{id} — protegida
POST /produtos — protegida
GET /produtos
GET /produtos/{id}
PUT /produtos/{id} — protegida
DELETE /produtos/{id} — protegida
POST /usuarios
POST /login
GET /usuarios/me — protegida
PUT /usuarios/me — protegida
POST /lancamentos — protegida
GET /lancamentos
GET /lancamentos/{id}

Próximos passos

DELETE e PUT de Lançamentos
Tratamento de erros global
Swagger documentado
Deploy
