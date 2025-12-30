from typing import List
from fastapi import APIRouter , Depends, Response , status , HTTPException
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
async def get_roles(db:Session = Depends(get_db)):
    roles_query = db.query(models.EmployeeRole).all()
    
    if roles_query != None:
        return roles_query
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Roles not found")

@router.get('/{id}' , response_model=schemas.IndividualRole)
async def get_role(id:int , db: Session=Depends(get_db)):
    role_query = db.query(models.EmployeeRole).filter(models.EmployeeRole.id == id)
    results = role_query.first()

    if results == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Role note found")
    
    return results

@router.delete('/{id}')
async def delete_role(id: int , db:Session=Depends(get_db)):

    delete_query = db.query(models.EmployeeRole).filter(models.EmployeeRole.id == id)
    results = delete_query.first()

    if results != None:
        db.delete(results)
        db.commit()
        db.close()

        return Response(status_code=status.HTTP_404_NOT_FOUND)
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail=f"Id {id} not found")
    
    