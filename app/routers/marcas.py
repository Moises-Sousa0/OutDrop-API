from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from typing import List
from app import auth


router = APIRouter() #cria um instancia da lib apirouter
 

#criar marca
@router.post("/marcas", status_code=201, response_model=schemas.MarcaResponse) #o @ é um decorator, ele basicamente diz "quando chegar um request em /marcas execute essa funcao:"
def criar_marca(marca: schemas.MarcaCreate, usuario_id = Depends(auth.verificar_token), db: Session = Depends(get_db)): #parametro marca pede o padrao da classe marcacreate, nome e descric
    atribuir_marca = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if atribuir_marca.marca_id is not None:
        raise HTTPException(status_code=403, detail="Não é possivel ter mais de uma marca por usuario ainda...")
    nova_marca = models.Marca( #Depends é o sistema de injeção de dependencia do fastapi 
        nome=marca.nome,
        descricao=marca.descricao,
    )
    db.add(nova_marca) #insere marca no banco
    db.commit() #salva marca no banco
    db.refresh(nova_marca) #pega os atributos do banco que não existem no objeto python e sincroniza o objeto com o banco
    atribuir_marca.marca_id=nova_marca.id
    db.commit()
    db.refresh(atribuir_marca)
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
def deletar_marca(id: int, usuario_id = Depends(auth.verificar_token), db: Session = Depends(get_db)):
    resultado_marca = db.query(models.Marca).filter(models.Marca.id == id).first()
    resultado_usuario = db.query(models.Usuario).filter(models.Usuario.marca_id == id, models.Usuario.id == usuario_id).first()

    if resultado_marca is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    
    if resultado_usuario is None:
        raise HTTPException(status_code=403, detail=f"{resultado_marca.nome} não pertence ao usuario") 

    resultado_usuario.marca_id = None    
    db.delete(resultado_marca)
    db.commit()
    return {"message": f"Marca {resultado_marca.nome} foi deletada com sucesso!"}

#atualizar marca
@router.put("/marcas/{id}")
def atualizar_marcas(id: int, marca: schemas.MarcaUpdate, usuario_id = Depends(auth.verificar_token),  db: Session = Depends(get_db)):
    verificar_marca = db.query(models.Marca).filter(models.Marca.id == id).first()
    verificar_usuario = db.query(models.Usuario).filter(models.Usuario.marca_id == id, models.Usuario.id == usuario_id).first()

    if verificar_marca is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada :(")
    
    if verificar_usuario is None:
        raise HTTPException(status_code=403, detail=f"{verificar_marca.nome} não pertence ao usuario")

    marca_nova = marca.model_dump(exclude_unset=True)
    for campo, valor in marca_nova.items():
        setattr(verificar_marca, campo, valor)

    db.commit()
    db.refresh(verificar_marca)
    
    return verificar_marca