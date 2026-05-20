from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from passlib.context import CryptContext 

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

@router.post("/usuarios", status_code=201, response_model=schemas.UsuarioResponse)
def criar_usuario(usuario: schemas.UsuarioCreate, db: Session = Depends(get_db)):
    verificar_email = db.query(models.Usuario).filter(models.Usuario.email == usuario.email).first()
    if verificar_email is not None:
        raise HTTPException(status_code=400, detail="Já existe uma conta com esse email")
    novo_usuario = models.Usuario(
        nome=usuario.nome,
        email=usuario.email,
        hash_senha=pwd_context.hash(usuario.senha)
        

    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario