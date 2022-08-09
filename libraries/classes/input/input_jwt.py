from fastapi import Depends
from pydantic import BaseModel
from app.base_schemas import UserBase
from libraries.utils.auth_bearer import JWTBearer
from libraries.utils.token_jwt import get_current_user

class InputJWT(BaseModel):
    user_session: UserBase

def input_jwt(
    user_session: UserBase = Depends(JWTBearer()),
    ):
    return InputJWT(
        user_session=user_session
    )
