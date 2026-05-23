from fastapi import FastAPI #cria aplicacao web / servidor
from app.routers import marcas #importa a rota "marcas"
from app.routers import produtos #importa a rota "produtos"
from app.routers import usuarios
from app.routers import lancamentos
from app.database import engine
from app import models

app = FastAPI() #aplicacao printicipal

models.Base.metadata.create_all(bind=engine) #chama o sqlaclhemy e manda verificar todos os modelos que existem e cria as tabaelas que ainda n existem


app.include_router(marcas.router) #conecta o router do marcas.py na aplicacao principal (main.py) (PEGA TODAS AS ROTAS DO ARQUIVOS marcas.py)
app.include_router(produtos.router) #conecta o router do produtos.py na aplicacao principal (main.py) (PEGA TODAS AS ROTAS DO ARQUIVOS produtos.py)
app.include_router(usuarios.router)
app.include_router(lancamentos.router)

@app.get("/health") #cria rota get
def health_check():
    return{"status": "Ok"}

