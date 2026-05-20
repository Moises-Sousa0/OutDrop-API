from jose import jwt
from datetime import datetime, timedelta
from dotenv import load_dotenv
import os

load_dotenv()
SECRET_KEY = os.getenv("SECRET_KEY")
ALOGRITHM = os.getenv("ALOGRITHM")



def criar_token(dados: dict):
    payload = dados.copy()
    expiracao = datetime.utcnow() + timedelta(minutes=30)
    payload.update({"exp": expiracao})
    return jwt.encode(payload, SECRET_KEY, algorithm=ALOGRITHM)