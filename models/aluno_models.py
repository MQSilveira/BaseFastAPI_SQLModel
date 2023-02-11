from typing import Optional
from sqlmodel import Field, SQLModel

class AlunoModel(SQLModel, table=True):
    __tablename__ = 'alunos'

    id:Optional[int] = Field(default=None, primary_key=True)
    nome : str
    email : str
    
    
