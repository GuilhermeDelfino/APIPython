from fastapi import APIRouter
from controller import TelefoneController
router = APIRouter()

@router.get('/get')
def get():
    return TelefoneController.getNumber()
    
@router.get('/get/{id}')
def getById(id: int):
    return TelefoneController.getNumber()
    
@router.post('/insert')
def insert():
    return TelefoneController.insertNumber()
    
@router.put('/update')
def update():
    return TelefoneController.updateNumber()
    
@router.delete('/delete')
def delete():
    return TelefoneController.deleteUser()