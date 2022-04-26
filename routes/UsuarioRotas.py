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
    cursor = con.cursor()

    sql = "SELECT * FROM Usuario WHERE idUsuario = %s"

    cursor.execute(sql, (id,))

    data = cursor.fetchone()

    return {
        "status": 200,
        "message": f"{cursor.rowcount} usuário selecionado.",
        "data":  data
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

    
@router.put('/update/{id}')
def update(user: User, id: int):
    cursor = con.cursor()

    sql = "UPDATE Usuario SET nome = %s WHERE idUsuario = %s"
    val = (user.nome, id)

    cursor.execute(sql, val)

    con.commit()
    cursor.close()

    return {
        "status": 200,
        "message": f"Usuário {user.nome} com id = {id} atualizado."
    }
    
@router.delete('/delete/{id}')
def delete(id: int):
    cursor = con.cursor()

    sql = "DELETE FROM Usuario WHERE idUsuario = %s"

    cursor.execute(sql, (id,))

    con.commit()

    return {
        "status": 200,
        "message": f"{cursor.rowcount} usuário excluído.",
    }