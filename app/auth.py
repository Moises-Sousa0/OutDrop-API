from jose import jwt, JWTError
from datetime import datetime, timedelta, timezone
from dotenv import load_dotenv
from fastapi.security import OAuth2PasswordBearer
from fastapi import Depends, HTTPException
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALGORITHM = os.getenv("ALGORITHM")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login") #extrai o token do cabeçalho



def criar_token(dados: dict):
    payload = dados.copy() #
    expiracao = datetime.now(timezone.utc) + timedelta(minutes=30)
    payload.update({"exp": expiracao})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALGORITHM)


def verificar_token(token: str = Depends(oauth2_scheme)): #recebe token do cabeçalho
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM]) #decodifica com secret_key
        user_id = payload.get("sub") #extrai o sub do payload
        if user_id is None: #verifica se o sub é valido
            raise HTTPException(status_code=401, detail="Login invalido")
    except JWTError: #se o token for invalido ou expirado, retorna erro
        raise HTTPException(status_code=401, detail="Token invalido ou expirado")
    
    return user_id #se der certo retorna o id do usuario