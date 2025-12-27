from typing import List
from fastapi import APIRouter , Depends , status , HTTPException
from sqlalchemy.orm import Session
from .. import models , schemas
from ..database import get_db

router = APIRouter(
    prefix="/roles",
    tags= ["Role"]
)

@router.post("/")
async def create_role(role:schemas.CreateRoles , db: Session = Depends(get_db)):

    role_query = models.EmployeeRole(**role.dict())

    if role_query !=None:
        db.add(role_query)
        db.commit()
        db.refresh(role_query)

        return role_query

    else:
        raise HTTPException(status_code=status.HTTP_204_NO_CONTENT , detail="Nothing to create") 
      
@router.get("/" , response_model=List[schemas.RoleResponse])
async def get_role():
    pass