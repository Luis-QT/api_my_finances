""" Defines the input schema of the API Login """
from fastapi import Body
from pydantic import BaseModel

class LoginBody(BaseModel):
    """ Body API """
    email: str = Body(..., example="admin@admin.com")
    password: str = Body(..., example="123456")

class LoginQuery(BaseModel):
    """ Query API """

class LoginHeader(BaseModel):
    """ Header API """

class LoginPath(BaseModel):
    """ Path API """

class LoginInput(
    LoginBody,
    LoginQuery,
    LoginHeader,
    LoginPath
):
    """ Input API """
