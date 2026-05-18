from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from pydantic import BaseModel #permite o fastapi validar automaticamente os dados recebidos
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from datetime import datetime
from decimal import Decimal

router = APIRouter()

class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: Decimal
    data_lancamento: datetime
    marca_id: int


@router.post("/produtos")
def criar_produto(produto: ProdutoCreate, db: Session = Depends(get_db)):
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
    return(novo_produto)


#listar produtos
@router.get("/produtos")
def listar_produtos(db: Session = Depends(get_db)):
    listar = db.query(models.Produto).all()
    return listar


#listar produtos especificos
@router.get("/produtos/{id}")
def buscar_produtos(id: int, db: Session = Depends(get_db)):
    buscar_produtos = db.query(models.Produto).filter(models.Produto.id == id).first()
    if buscar_produtos is None:
        raise HTTPException(status_code=404, detail="Marca não encontrada :(")
    return buscar_produtos