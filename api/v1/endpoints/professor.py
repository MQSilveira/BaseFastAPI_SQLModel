from typing import List

from fastapi import APIRouter
from fastapi import status
from fastapi import Depends
from fastapi import HTTPException
from fastapi import Response

from sqlalchemy.ext.asyncio import AsyncSession
from sqlmodel import select
from models.professor_model import ProfessorModel
from core.deps import get_session

# Bypass warning SQLModel select
from sqlmodel.sql.expression import Select, SelectOfScalar
SelectOfScalar.inherit_cache = True
Select.inherit_cache = True
# Fim Bypass


router = APIRouter()

#POST professor
@router.post('/', status_code=status.HTTP_201_CREATED, response_model=ProfessorModel)
async def post_professor(professor:ProfessorModel, db:AsyncSession=Depends(get_session)):
    
    novo_professor = ProfessorModel(
        nome = professor.nome,
        email = professor.email,
    )
    
    db.add(novo_professor)
    await db.commit()
    
    return professor


#GET professor
@router.get('/', response_model=List[ProfessorModel])
async def get_professor(db:AsyncSession=Depends(get_session)):
    async with db as session:
        
        query = select(ProfessorModel)
        result = await session.execute(query)
        professores:List[ProfessorModel] = result.scalars().all()
        
        return professores


# GET professor
@router.get('/{professor_id}', response_model=ProfessorModel, status_code=status.HTTP_200_OK)
async def get_professor(professor_id:int, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor = result.scalar_one_or_none()
        
        if professor:
            return professor
        
        raise HTTPException(
            detail='Professor não encontrado!',
            status_code=status.HTTP_404_NOT_FOUND
            )


# PUT professor
@router.put('/{professor_id}', response_model=ProfessorModel, status_code=status.HTTP_202_ACCEPTED)
async def put_professor(professor_id:int, professor:ProfessorModel, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor_up = result.scalar_one_or_none()
        
        if professor_up:
            professor_up.nome = professor.nome
            professor_up.email = professor.email

            await session.commit()
            
            return professor_up
        
        raise HTTPException(
            detail='Professor não encontrado!',
            status_code=status.HTTP_404_NOT_FOUND
            )


# DELETE
@router.delete('/{professor_id}', status_code=status.HTTP_204_NO_CONTENT)
async def delete_professor(professor_id:int, db:AsyncSession=Depends(get_session)):
    async with db as session:
        query = select(ProfessorModel).filter(ProfessorModel.id == professor_id)
        result = await session.execute(query)
        professor_del = result.scalar_one_or_none()
        
        if professor_del:
            await session.delete(professor_del)
            await session.commit()
            
            return Response(status_code=status.HTTP_204_NO_CONTENT)
        
        raise HTTPException(
            detail='Professor não encontrado!',
            status_code=status.HTTP_404_NOT_FOUND
            )


