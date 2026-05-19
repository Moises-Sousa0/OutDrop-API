from pydantic import BaseModel 
from datetime import datetime
from decimal import Decimal

#schemas é onde pode configurar oq o usuario pode enviar e controlar oq a API mostra

#saida e entrada da tabela marcas
class MarcaCreate(BaseModel): #pydanticacho
    nome: str
    descricao: str


class MarcaResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    created_at: datetime
    class Config:
        from_attributes = True


#saida e entrada da tabela usuarios
class UsuarioCreate(BaseModel):
    nome: str
    email: str
    senha: str
    
class UsuarioResponse(BaseModel):
    id: int
    nome: str
    email: str
    class Config:
        from_attributes = True #pydantic agr vai aceitar objetos do sqlalchemy
    

#saida e entrada da tabela produtos
class ProdutoCreate(BaseModel):
    nome: str
    descricao: str
    preco: Decimal
    data_lancamento: datetime
    marca_id: int


class ProdutoResponse(BaseModel):
    id: int
    nome: str
    descricao: str
    marca_id: int
    class Config:
        from_attributes = True
