""" User Schema """
from uuid import UUID
from datetime import datetime
from pydantic import BaseModel

class UserBase(BaseModel):
    """ User data """
    id: UUID
    name: str
    email: str
    avatar_url: str
