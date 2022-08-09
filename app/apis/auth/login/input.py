""" Define las clases de entrada de la API register """
from fastapi import Depends
from pydantic import BaseModel, Field

from libraries.classes.input.input_api import InputAPI, input_api

class LoginBody(BaseModel):
    email: str = Field(..., example="admin@admin.com")
    password: str = Field(..., example="123456")

class LoginInput(InputAPI, LoginBody):
    pass

def login_input(
    body: LoginBody,
    input_api: InputAPI = Depends(input_api)
    ):
    return LoginInput.parse_obj({
        **input_api.dict(),
        **body.dict()
    })
