from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from typing import List



router = APIRouter() #cria um instancia da lib apirouter
 



@router.post("/marcas", status_code=201, response_model=schemas.MarcaResponse) #o @ é um decorator, ele basicamente diz "quando chegar um request em /marcas execute essa funcao:"
def criar_marca(marca: schemas.MarcaCreate, db: Session = Depends(get_db)): #parametro marca pede o padrao da classe marcacreate, nome e descric
    nova_marca = models.Marca( #Depends é o sistema de injeção de dependencia do fastapi 
        nome=marca.nome,
        descricao=marca.descricao
    )
    db.add(nova_marca) #insere marca no banco
    db.commit() #salva marca no banco
    db.refresh(nova_marca) #pega os atributos do banco que não existem no objeto python e sincroniza o objeto com o banco
    return nova_marca


#listar todas as marcas
@router.get("/marcas", response_model=List[schemas.MarcaResponse]) #List serve pra informar q a resposta vai ser uma lista de marcas
def ver_marcas(db: Session = Depends(get_db)):
    return db.query(models.Marca).all()

#listar marca especifica
@router.get("/marcas/{id}", response_model=schemas.MarcaResponse)
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