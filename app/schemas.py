from pydantic import BaseModel , EmailStr
from typing import List
from datetime import datetime

from sqlalchemy import DATETIME


"""CREATE EMPLOYEE"""

class CreateEmployee(BaseModel):
    firstname: str
    age: int
    created_at: datetime

class EmployeeRes(CreateEmployee):
    id:int
    class Config:
        from_attribute = True

"""ADDING ROLES"""

class CreateRoles(BaseModel):
    position: str
    started_at : datetime
    earning: int
    owner_id: int

class RoleResponse(BaseModel):
    position: str
    started_at: datetime
    owner_id:int

    class Config:
        from_attribute = True