from datetime import datetime
from fastapi import APIRouter #agrupa rotas do mesmo recurso
from pydantic import BaseModel #permite o fastapi validar automaticamente os dados recebidos

router = APIRouter() #cria um instancia da lib apirouter

class MarcaCreate(BaseModel):
    nome: str
    descricao: str

marcas = []

@router.post("/marcas") #o @ é um decorator, ele basicamente diz "quando chegar um requisi POST em /marcas execute essa funcao:"
def criar_marca(marca: MarcaCreate): #parametro marca pede o padrao da classe marcacreate, nome e descric
    nova_marca = {
        "id": len(marcas) + 1,
        "nome": marca.nome,
        "descricao": marca.descricao,
        "created_at": datetime.now().isoformat()
    }
    marcas.append(nova_marca)
    return nova_marca