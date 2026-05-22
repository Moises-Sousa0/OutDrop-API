from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from typing import List


router = APIRouter()



@router.post("/produtos", status_code=201, response_model=schemas.ProdutoResponse)
def criar_produto(produto: schemas.ProdutoCreate, db: Session = Depends(get_db)):
    marca = db.query(models.Marca).filter(models.Marca.id == produto.marca_id).first()
    if marca is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada")
    novo_produto = models.Produto(
        nome=produto.nome,
        descricao=produto.descricao,
        preco=produto.preco,
        data_lancamento=produto.data_lancamento,
        marca_id=produto.marca_id
    )
    db.add(novo_produto)
    db.commit()
    db.refresh(novo_produto)
    return novo_produto


#listar todos os produtos
@router.get("/produtos", response_model=List[schemas.ProdutoResponse])
def listar_produtos(db: Session = Depends(get_db)):
    return db.query(models.Produto).all()
    


#listar produtos especificos
@router.get("/produtos/{id}", response_model=schemas.ProdutoResponse)
def buscar_produtos(id: int, db: Session = Depends(get_db)):
    ver_produtos = db.query(models.Produto).filter(models.Produto.id == id).first()
    if ver_produtos is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado :(")
    return ver_produtos

#deletar produtos
@router.delete("/produtos/{id}")
def deletar_produto(id: int, db: Session = Depends(get_db)):
    escolher_produto = db.query(models.Produto).filter(models.Produto.id == id).first()
    if escolher_produto is None:
            raise HTTPException(status_code=404, detail="Produto não encontrado :(")
    db.delete(escolher_produto)
    db.commit()
    return {"message": f"Produto {escolher_produto.nome} foi deletado com sucesso!"}

#atualizar produtos
@router.put("/produtos/{id}")
def atualizar_produtos(id: int, produto: schemas.ProdutoUpdate, db: Session = Depends(get_db)):
    verificar_produto = db.query(models.Produto).filter(models.Produto.id == id).first()
    if verificar_produto is None:
        raise HTTPException(status_code=404, detail="Produto não encontrado :(")
    campos_novos = produto.model_dump()

    for campo, valor in campos_novos.items():
        setattr(verificar_produto, campo, valor)    

    db.commit()
    db.refresh(verificar_produto)
    return verificar_produto