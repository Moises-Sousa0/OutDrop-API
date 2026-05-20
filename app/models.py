from sqlalchemy import Column, Integer, String, DateTime, ForeignKey, Numeric
from datetime import datetime
from app.database import Base


class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)  #nullable = notnull
    descricao = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)


class Produto(Base):
    __tablename__ = "produtos"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    preco = Column(Numeric, nullable=False)
    descricao = Column(String, nullable=False)
    data_lancamento = Column(DateTime, nullable=False)
    marca_id = Column(Integer, ForeignKey("marcas.id"), nullable=False)


class Usuario(Base):
    __tablename__ = "usuarios"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)
    email = Column(String, nullable=False, unique=True)
    hash_senha = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)