from fastapi import FastAPI
from app.routers import marcas

app = FastAPI()

app.include_router(marcas.router) #conecta o router do marcas.py na aplicacao principal (main.py)

@app.get("/health")
def health_check():
    return{"status": "Ok"}

