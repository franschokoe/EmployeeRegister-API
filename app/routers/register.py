from typing import List
from fastapi import APIRouter , Depends , status ,HTTPException
from sqlalchemy.orm import Session
from ..database import get_db
from .. import models
from .. import schemas

router = APIRouter(
    prefix="/employee" ,    
    tags=['register']
)


# register a employee


@router.post("/" ,status_code=status.HTTP_201_CREATED , response_model= schemas.EmployeeRes)
async def create_employee(employee: schemas.CreateEmployee,db: Session = Depends(get_db)):
    # employee_query = db.query(models.EmployeeRegister)
    employee_query = models.EmployeeRegister(**employee.dict())

    if employee_query != None:

        db.add(employee_query)
        db.commit()
        db.refresh(employee_query)

        return employee_query
    else :
        raise HTTPException(status_code=status.HTTP_409_CONFLICT , detail="Fill all")
    

@router.get("/" , response_model=List[schemas.EmployeeRes])
async def get_employees(db: Session = Depends(get_db)):

    employees_query = db.query(models.EmployeeRegister).all()

    if employees_query == None:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Employees not found")
    
    return employees_query


@router.get("/{id}")
async def employee(id:int , db:Session = Depends(get_db)):
    employee_query = db.query(models.EmployeeRegister).filter(models.EmployeeRegister.id == id)
    employee_results = employee_query.first()

    if employee_results == None:

        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND , detail="Not Found")

    else:
        return employee_results
    

@router.delete("/{id}")
async def remove_employee(id: int , db: Session= Depends(get_db)):

    employee_query = db.query(models.EmployeeRegister).filter(models.EmployeeRegister.id == id)

    employee_results = employee_query.first()

    if employee_results != None:

        db.delete(employee_results)
        db.commit()
        db.close()

        return {"data" : f"employee {id} deleted"}
    
    else:
        raise HTTPException(status_code=404 , detail=f"User {id} Not Found")
    