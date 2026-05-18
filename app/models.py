from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Marca(Base):
    __tablename__ = "marcas"

    id = Column(Integer, primary_key=True, index=True)
    nome = Column(String, nullable=False)  #nullable = notnull
    descricao = Column(String, nullable=False)
    created_at = Column(DateTime, default=datetime.now)