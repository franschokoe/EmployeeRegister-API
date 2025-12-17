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
    pass