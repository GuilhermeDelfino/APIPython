from fastapi import APIRouter
from database.conexao import Connection
from model.UsuarioModel import User

con = Connection('aluno', 'sptech', 'Agenda').getConnection()
router = APIRouter()

@router.get('/get')
def getUsers():
    cursor = con.cursor()

    sql = "SELECT * FROM Usuario"

    cursor.execute(sql)

    data = cursor.fetchall()

    return {
        "status": 200,
        "message": f"{cursor.rowcount} usuários selecionados.",
        "data":  data
    }
   
@router.get('/get/{id}')
def getUserById(id: int):
    return {
        "status": 200
    }
    
@router.post('/insert')
def setUser(user: User) :
    cursor = con.cursor()
    

    sql = "INSERT INTO usuario (nome) VALUES (%s)"
    val = (user.nome,)

    cursor.execute(sql, val)

    con.commit()
    cursor.close()

    return {
        "status": 200,
        "message": f"Usuário {user.nome} cadastrado com sucesso."
    }

    
@router.put('/update')
def update():
    return {
        "status": 200
    }
    
@router.delete('/delete')
def delete():
    return {
        "status": 200
    }