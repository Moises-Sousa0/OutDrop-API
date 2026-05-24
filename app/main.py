from fastapi import FastAPI, Request, HTTPException #FastAPI cria aplicacao web / servidor
from fastapi.responses import JSONResponse
from sqlalchemy.exc import OperationalError 
from fastapi.exceptions import RequestValidationError
from app.routers import marcas #importa a rota "marcas"
from app.routers import produtos #importa a rota "produtos"
from app.routers import usuarios, lancamentos
from app.database import engine

from app import models



app = FastAPI() #aplicacao printicipal

models.Base.metadata.create_all(bind=engine) #chama o sqlaclhemy e manda verificar todos os modelos que existem e cria as tabaelas que ainda n existem


app.include_router(marcas.router, tags=["Marcas"]) #conecta o router do marcas.py na aplicacao principal (main.py) (PEGA TODAS AS ROTAS DO ARQUIVOS marcas.py)
app.include_router(produtos.router, tags=["Produtos"]) #conecta o router do produtos.py na aplicacao principal (main.py) (PEGA TODAS AS ROTAS DO ARQUIVOS produtos.py)
app.include_router(usuarios.router, tags=["Usuarios"])
app.include_router(lancamentos.router, tags=["Lancamentos"])

@app.exception_handler(OperationalError)
async def db_error_handler(request: Request, exc: OperationalError):
    return JSONResponse(
        status_code=503,
        content={"detail": "Serviço indisponivel. Tente novamente mais tarde"}
    )

@app.exception_handler(RequestValidationError)
async def error_request(request: Request, exc: RequestValidationError):
    return JSONResponse(
        status_code=422,
        content={"detail": "Request inválida"}
    )

@app.exception_handler(HTTPException)
async def error_404(request: Request, exc: HTTPException):
    if exc.status_code == 404:
        return JSONResponse(
            status_code=404,
            content={"detail": "Sem resultados para esse request"}  
        )
    else:
        return JSONResponse(
            status_code=exc.status_code,
            content={"detail": exc.detail}
        )  

@app.get("/health", tags=["Health"]) #cria rota get
def health_check():
    return{"status": "Ok"}

