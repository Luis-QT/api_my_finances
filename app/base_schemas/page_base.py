""" Page Base Schema """
from pydantic import BaseModel

class PageBase(BaseModel):
    """ Page Data """
    limit: int
    page: int
    pages: int
    total: int
