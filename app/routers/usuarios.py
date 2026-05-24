from fastapi import APIRouter, HTTPException, Depends #agrupa rotas do mesmo recurso
from sqlalchemy.orm import Session
from app.database import get_db
from app import models
from app import schemas
from passlib.context import CryptContext 
from fastapi.security import OAuth2PasswordRequestForm
from app import auth
from sqlalchemy import or_

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
        hash_senha=pwd_context.hash(usuario.senha) #transforma a senha em hash ah en
    )
    db.add(novo_usuario)
    db.commit()
    db.refresh(novo_usuario)
    return novo_usuario

#login usuarios
@router.post("/login", response_model=schemas.TokenResponse)  
def login(form_data: OAuth2PasswordRequestForm = Depends(), db: Session = Depends(get_db)):
    verificar_username = db.query(models.Usuario).filter(or_(models.Usuario.email == form_data.username, models.Usuario.nome == form_data.username)).first()
    if verificar_username is None:
        raise HTTPException(status_code=401, detail="Usuario ou senha errados")
    senha_correta = pwd_context.verify(form_data.password, verificar_username.hash_senha )
    if not senha_correta:
        raise HTTPException(status_code=401, detail="Usuario ou senha errados")
    token = auth.criar_token({"sub": str(verificar_username.id)})
    return {"access_token": token, "token_type": "bearer"}


#seguranca_rota
@router.get("/usuarios/me", response_model=schemas.UsuarioResponse)
def me_rota(usuario_id = Depends(auth.verificar_token), db: Session = Depends(get_db)): #obriga o token ser validado antes de executar
    usuario = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if usuario is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    
    return usuario

@router.put("/usuarios/me", response_model=schemas.UsuarioResponse)
def me_update(usuario: schemas.UsuarioUpdate, usuario_id =  Depends(auth.verificar_token), db: Session = Depends(get_db)):
    verificar = db.query(models.Usuario).filter(models.Usuario.id == usuario_id).first()
    if verificar is None:
        raise HTTPException(status_code=404, detail="Usuario não encontrado")
    infos_pessoais = usuario.model_dump(exclude_unset=True) #pega os dados do usuario e transforma em dicionario, excluindo os campos que não foram enviados
    if "senha" in infos_pessoais:
        infos_pessoais["hash_senha"] = pwd_context.hash(
            infos_pessoais["senha"]
        )
        del infos_pessoais["senha"]
    
    for campo, valor in infos_pessoais.items():
        setattr(verificar, campo, valor)
    
    db.commit()
    db.refresh(verificar)

    return verificar