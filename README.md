# OUTDROP API
API para gerenciamento de drops de marcas de roupas - sendo possível cadastrar marcas, produtos e lançamentos.


## Tecnologias
- Python
- FastAPI
- PostgreSQL (em breve)

## Rotas disponiveis
- GET /health
- POST /marcas

## Próximos passos
- Adicionar banco de dados (PostgreSQL)
- Adicionar mais rotas
- Area de login
- Autenticação JWT

## Como rodar localmente
1. Clone o repositório
2. Crie e ative o ambiente virtual:
   python -m venv venv
   venv\Scripts\activate
3. Instale as dependências:
   pip install -r requirements.txt
4. Rode o servidor:
   uvicorn app.main:app --reload
5. Acesse a documentação em  http://127.0.0.1:8000/docs
