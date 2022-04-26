from fastapi import FastAPI
from routes import UsuarioRotas, TelefoneRotas

app = FastAPI()

app.include_router(UsuarioRotas.router, prefix='/usuario')
app.include_router(TelefoneRotas.router, prefix='/telefone')
