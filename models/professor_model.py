from typing import Optional
from sqlmodel import Field, SQLModel


class ProfessorModel(SQLModel, table=True):
    __tablename__ = 'professores'

    id:Optional[int] = Field(default=None, primary_key=True)
    nome : str
    email : str
    
    