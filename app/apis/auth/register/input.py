""" Define las clases de entrada de la API Register """
from fastapi import Body
from pydantic import BaseModel

class RegisterBody(BaseModel):
    name: str = Body(..., example="test")
    email: str = Body(..., example="test@test.com")
    password: str = Body(..., example="password")

class RegisterQuery(BaseModel):
    pass

class RegisterHeader(BaseModel):
    pass

class RegisterPath(BaseModel):
    pass

class RegisterInput(
    RegisterBody,
    RegisterQuery,
    RegisterHeader,
    RegisterPath
):
    pass
