from fastapi import APIRouter
from api.v1.endpoints import aluno
from api.v1.endpoints import professor
from api.v1.endpoints import usuario


api_router = APIRouter()

api_router.include_router(aluno.router, prefix='/alunos', tags=['alunos'])
api_router.include_router(professor.router, prefix='/professores', tags=['professores'])
api_router.include_router(usuario.router, prefix='/usuarios', tags=['usuarios'])

