from fastapi import APIRouter

router = APIRouter()

@router.get('/get')
def get():
    return {
        'status': 200
    }
    
@router.get('/get/{id}')
def getById(id: int):
    return {
        'status': 200
    }
    
@router.post('/insert')
def insert():
    return {
        'status': 200
    }
    
@router.put('/update')
def update():
    return {
        'status': 200
    }
    
@router.delete('/delete')
def delete():
    return {
        'status': 200
    }