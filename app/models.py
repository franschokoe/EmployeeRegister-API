from pydantic import BaseModel
from sqlalchemy import Column, DATETIME , Integer , String , TIMESTAMP, func, text ,ForeignKey , PrimaryKeyConstraint
from sqlalchemy.orm import relationship
from app.database import Base
from datetime import timedelta

# Employee Model
class EmployeeRegister(Base):
    # table name
    __tablename__ = "employees"    
    # columns
    id = Column(Integer , nullable=False , primary_key=True , index=True)
    firstname = Column(String , nullable=False)
    age = Column(Integer , nullable=False)
    created_at = Column(TIMESTAMP(timezone=False) , server_default=text("NOW()"))
    
    
# Role Model
class EmployeeRole(Base):
    __tablename__ = "roles"
    id = Column(Integer , nullable=False , primary_key=True , index=True)
    position = Column(String , nullable=False)
    started_at = Column(TIMESTAMP(timezone=True) , nullable=False , server_default=text("now()"))
    earning = Column(Integer , nullable=False)
    owner_id = Column(Integer , ForeignKey("employees.id" , ondelete="CASCADE") , nullable=True)
    owner = relationship("EmployeeRegister")