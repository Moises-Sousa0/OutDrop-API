from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from passlib.context import CryptContext 
from fastapi.security import OAuth2PasswordRequestForm
from app import auth

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
router = APIRouter()

#criar usuarios
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

#login usuarios
@router.post("/login", response_model=schemas.TokenResponse)  
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    verififcar_email = db.query(models.Usuario).filter(models.Usuario.email == form_data.username).first()
    if verififcar_email is None:
        raise HTTPException(status_code=401, detail="Usuario ou senha errados")
    senha_correta = pwd_context.verify(form_data.password, verififcar_email.hash_senha )
    if not senha_correta:
        raise HTTPException(status_code=401, detail="Usuario ou senha errados")
    token = auth.criar_token({"sub": verififcar_email.id})
    return {"access_token": token, "token_type": "bearer"}