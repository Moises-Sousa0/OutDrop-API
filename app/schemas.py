from pydantic import BaseModel 

class MarcaCreate(BaseModel): #pydanticacho
    nome: str
    descricao: str