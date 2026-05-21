from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, declarative_base
from dotenv import load_dotenv
import os

load_dotenv()

DATABASE_URL = os.getenv("DATABASE_URL")

engine = create_engine(DATABASE_URL) #cria conexao com postgresql, engine é o objeto que o sqlaclhemy usa pra se comunica com banco

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine) #cria sessoes com o banco

Base = declarative_base() #classe base q todos models herdam, permite enxegar as tabelas

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()