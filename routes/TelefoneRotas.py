from fastapi import APIRouter
from database.conexao import Connection
from model.TelefoneModel import Telefone

con = Connection().getConnection()
router = APIRouter()


@router.get('/get')
async def get():
    cursor = con.cursor()

    sql = "SELECT * FROM Telefone"

    cursor.execute(sql)

    data = cursor.fetchall()

    return {
        "status": 200,
        "message": f"{cursor.rowcount} telefones selecionados.",
        "data":  data
    }


@router.get('/get/{id}')
async def getById(id: int):
    cursor = con.cursor()

    sql = "SELECT * FROM Usuario WHERE idUsuario = %s"

    cursor.execute(sql, (id,))

    data = cursor.fetchone()

    return {
        "status": 200,
        "message": f"{cursor.rowcount} telefone selecionado.",
        "data":  data
    }


@router.post('/insert')
async def insert(telefone: Telefone):
    cursor = con.cursor()

    sql = "INSERT INTO telefone (numero, fkUsuario) VALUES (%s, %s)"
    val = (telefone.numero, telefone.user)

    cursor.execute(sql, val)

    con.commit()
    cursor.close()

    return {
        "status": 200,
        "message": f"Telefone {telefone.numero} cadastrado no user id = {telefone.user}."
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
