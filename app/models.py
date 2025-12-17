from pydantic import BaseModel
from sqlalchemy import Column , Integer , String , TIMESTAMP, text
from app.database import Base
from datetime import timedelta

class EmployeeRegister(Base):
    # table name
    __tablename__ = "employees"    
    # columns
    id = Column(Integer , nullable=False , primary_key=True , index=True)
    firstname = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    created_at = Column(TIMESTAMP(timezone=False) , server_default=text("NOW()"))
    
