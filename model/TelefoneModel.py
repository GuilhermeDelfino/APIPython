from pydantic import BaseModel


class Telefone(BaseModel):
    user: int
    numero: str
