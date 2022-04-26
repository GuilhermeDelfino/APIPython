from fastapi import APIRouter
from controller import UsuarioController
router = APIRouter()

@router.get('/get')
def get():
    return UsuarioController.getUsers()
    
@router.get('/get/{id}')
def getById(id: int):
    return UsuarioController.getUser()
    
@router.post('/insert')
def insert():
    return UsuarioController.insertUser()
    
@router.put('/update')
def update():
    return UsuarioController.updateUser()
    
@router.delete('/delete')
def delete():
    return UsuarioController.deleteUser()