from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from pydantic import BaseModel #permite o fastapi validar automaticamente os dados recebidos
from sqlalchemy.orm import Session
from app.database import get_db
from app import models


router = APIRouter() #cria um instancia da lib apirouter
 
class MarcaCreate(BaseModel): #pydanticacho
    nome: str
    descricao: str


@router.post("/marcas", status_code=201) #o @ é um decorator, ele basicamente diz "quando chegar um request POST em /marcas execute essa funcao:"
def criar_marca(marca: MarcaCreate, db: Session = Depends(get_db)): #parametro marca pede o padrao da classe marcacreate, nome e descric
    nova_marca = models.Marca( #Depends é o sistema de injeção de dependencia do fastapi 
        nome=marca.nome,
        descricao=marca.descricao
    )
    db.add(nova_marca)
    db.commit()
    db.refresh(nova_marca)
    return nova_marca


#listar todas as marcas
@router.get("/marcas")
def ver_marcas(db: Session = Depends(get_db)):
    listar = db.query(models.Marca).all() #SELECT * FROM marcas;
    return listar


#listar marca especifica
@router.get("/marcas/{id}")
def buscar_marcas(id: int, db: Session = Depends(get_db)):
    resultado = db.query(models.Marca).filter(models.Marca.id == id).first()
    if resultado is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada :(") #forma correta de retornar pro fastapi um erro
    return resultado

        

#deletar marca especifica
@router.delete("/marcas/{id}")
def deletar_marca(id: int, db: Session = Depends(get_db)):
    resultado = db.query(models.Marca).filter(models.Marca.id == id).first()
    if resultado is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    db.delete(resultado)
    db.commit()
    return {"message": f"Marca {resultado.nome} foi deletada com sucesso!"}