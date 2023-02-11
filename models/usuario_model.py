from typing import Optional
from sqlmodel import Field, SQLModel


class UsuarioModel(SQLModel, table=True):
    __tablename__ = 'usuarios'

    id:Optional[int] = Field(default=None, primary_key=True)
    nome : str
    email : str
    
    