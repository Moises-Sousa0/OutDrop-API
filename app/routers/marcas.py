from datetime import datetime
from fastapi import APIRouter, HTTPException #agrupa rotas do mesmo recurso
from pydantic import BaseModel #permite o fastapi validar automaticamente os dados recebidos

router = APIRouter() #cria um instancia da lib apirouter
 
class MarcaCreate(BaseModel): #pydanticacho
    nome: str
    descricao: str

marcas = []

@router.post("/marcas") #o @ é um decorator, ele basicamente diz "quando chegar um request POST em /marcas execute essa funcao:"
def criar_marca(marca: MarcaCreate): #parametro marca pede o padrao da classe marcacreate, nome e descric
    nova_marca = {
        "id": len(marcas) + 1,
        "nome": marca.nome,
        "descricao": marca.descricao,
        "created_at": datetime.now().isoformat()
    }
    marcas.append(nova_marca)
    return nova_marca

#listar todas as marcas
@router.get("/marcas")
def ver_marcas():
    return marcas

#listar marca especifica
@router.get("/marcas/{id}")
def buscar_marcas(id: int):
    for i in  marcas:
        if i["id"] == id:
            return i
            
    else:
        raise HTTPException(status_code=404, detail="Marca não encontrada :(") #forma correta de retornar pro fastapi um erro


#deletar marca especifica
@router.delete("/marcas/{id}")
def deletar_marca(id: int):
    for i in marcas:
        if i["id"] == id:
            marcas.remove(i)
            return {"message": "Marca deletada com sucesso", "marca": i}
    else:
        raise HTTPException(status_code=404, detail="Marca não encontrada")