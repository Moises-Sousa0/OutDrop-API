from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from typing import List
from app import auth


router = APIRouter()

#listar lancamento
@router.get("/lancamentos", response_model=List[schemas.LancamentoResponse])
def ver_lancamentos(db: Session = Depends(get_db)):
    return db.query(models.Lancamento).all()

#listar lancamento especifico
@router.get("/lancamentos/{id}", response_model=schemas.LancamentoResponse)
def ver_lancamento(id: int, db: Session = Depends(get_db)):
    listar_lanc = db.query(models.Lancamento).filter(models.Lancamento.id == id).first()
    if listar_lanc is None:
        raise HTTPException(status_code=404, detail="Lançamento não encontrado :(")
    return listar_lanc

#criar lancamento
@router.post("/lancamentos", status_code=201, response_model=schemas.LancamentoResponse)
def criar_lancamento( lancamento: schemas.LancamentoCreate, usuario_id = Depends(auth.verificar_token), db: Session = Depends(get_db)):
    atribuir_lancamento = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    produto_ver = db.query(models.Produto).filter(models.Produto.id == lancamento.produto_id).first()

    if atribuir_lancamento.marca_id != produto_ver.marca_id:
        raise HTTPException(status_code=403, detail="não é permitido criar um lancamento sem ser o dono da marca")

    novo_lancamento = models.Lancamento( 
        nome=lancamento.nome,
        data_lancamento=lancamento.data_lancamento,
        produto_id=lancamento.produto_id,
        marca_id=atribuir_lancamento.marca_id,
        usuario_id=atribuir_lancamento.id
    )
    db.add(novo_lancamento)
    db.commit()
    db.refresh(novo_lancamento)
    return novo_lancamento
