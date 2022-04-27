from fastapi import APIRouter

router = APIRouter()

@router.get('/get')
async def get():
    return {
        'status': 200
    }
    
@router.get('/get/{id}')
async def getById(id: int):
    return {
        'status': 200
    }
    
@router.post('/insert')
async def insert():
    return {
        'status': 200
    }
    
@router.put('/update')
async def update():
    return {
        'status': 200
    }
    
@router.delete('/delete')
async def delete():
    return {
        'status': 200
    }