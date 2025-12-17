from pydantic import BaseModel , EmailStr
from typing import List
from datetime import datetime


"""CREATE EMPLOYEE"""

class CreateEmployee(BaseModel):
    firstname: str
    age: int
    created_at: datetime

class EmployeeRes(CreateEmployee):
    id:int
    class Config:
        from_attribute = True