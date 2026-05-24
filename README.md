# OutDrop API

API para gerenciamento de drops de marcas de roupas — sendo possível cadastrar marcas, produtos e lançamentos.

🔗 **API em produção:** https://outdrop-api-production.up.railway.app/docs

---

## Tecnologias

- **Python** + **FastAPI**
- **PostgreSQL** + **SQLAlchemy** + **psycopg2**
- **Pydantic** — validação de dados
- **Passlib (bcrypt)** — hash de senhas
- **Python-Jose** — autenticação JWT
- **Alembic** — migrations de banco de dados
- **Railway** — deploy com CI/CD automático

---

## Funcionalidades

- Cadastro e autenticação de usuários com JWT
- Cada usuário pode criar e gerenciar sua própria marca
- CRUD completo de marcas, produtos e lançamentos
- Proteção de rotas — apenas o dono da marca pode editar ou deletar seus recursos
- Migrations automáticas no deploy via Alembic

---

## Rotas disponíveis

### Usuários
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/usuarios` | Cadastro |
| POST | `/login` | Login — retorna JWT |
| GET | `/usuarios/me` | Dados do usuário autenticado |
| PUT | `/usuarios/me` | Atualizar nome, email ou senha |

### Marcas
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/marcas` | Criar marca (protegida) |
| GET | `/marcas` | Listar todas |
| GET | `/marcas/{id}` | Buscar por ID |
| PUT | `/marcas/{id}` | Editar (protegida, só dono) |
| DELETE | `/marcas/{id}` | Deletar (protegida, só dono) |

### Produtos
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/produtos` | Criar produto (protegida) |
| GET | `/produtos` | Listar todos |
| GET | `/produtos/{id}` | Buscar por ID |
| PUT | `/produtos/{id}` | Editar (protegida, só dono) |
| DELETE | `/produtos/{id}` | Deletar (protegida, só dono) |

### Lançamentos
| Método | Rota | Descrição |
|--------|------|-----------|
| POST | `/lancamentos` | Criar lançamento (protegida) |
| GET | `/lancamentos` | Listar todos |
| GET | `/lancamentos/{id}` | Buscar por ID |
| PUT | `/lancamentos/{id}` | Editar (protegida, só dono) |
| DELETE | `/lancamentos/{id}` | Deletar (protegida, só dono) |

### Outros
| Método | Rota | Descrição |
|--------|------|-----------|
| GET | `/health` | Status da API |

---

## Como rodar localmente

1. Clone o repositório
```bash
git clone https://github.com/seu-usuario/outdrop-api
cd outdrop-api
```

2. Crie e ative o ambiente virtual
```bash
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Linux/Mac
```

3. Instale as dependências
```bash
pip install -r requirements.txt
```

4. Configure o arquivo `.env` na raiz do projeto
```env
DATABASE_URL=postgresql://usuario:senha@localhost/nome_do_banco
SECRET_KEY=sua_chave_secreta
ALGORITHM=HS256
```

5. Rode as migrations
```bash
alembic upgrade head
```

6. Suba o servidor
```bash
uvicorn app.main:app --reload
```

7. Acesse a documentação em http://127.0.0.1:8000/docs