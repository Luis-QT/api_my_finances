""" Define las clases de entrada de la API Login """
from fastapi import Body
from pydantic import BaseModel
from pydantic import BaseModel

class LoginBody(BaseModel):
    email: str = Body(..., example="admin@admin.com")
    password: str = Body(..., example="123456")

class LoginQuery(BaseModel):
    pass

class LoginHeader(BaseModel):
    pass

class LoginPath(BaseModel):
    pass

class LoginInput(
    LoginBody,
    LoginQuery,
    LoginHeader,
    LoginPath
):
    pass

